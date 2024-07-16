import sqlite3
import feedparser
import yaml
import requests
import time
import datetime
import dingtalkchatbot.chatbot as cb
import telegram

# 加载配置文件
def load_config():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# 初始化数据库
def init_database():
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        link TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    return conn


# 获取数据并检查更新
def check_for_updates(feed_url, site_name, cursor, conn):
    print(f"{site_name} 监控中... ")
    data_list = []
    file_data = feedparser.parse(feed_url)
    data = file_data.entries
    if data:
        data_title = data[0].get('title')
        data_link = data[0].get('link')
        data_list.append(data_title)
        data_list.append(data_link)

        # 查询数据库中是否存在相同链接的文章
        cursor.execute("SELECT * FROM items WHERE link = ?", (data_link,))
        result = cursor.fetchone()
        if result is None:
            # 未找到相同链接的文章，进行推送
            push_message(f"{site_name}今日更新", f"标题: {data_title}\n链接: {data_link}\n\n\n推送时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")

            # 存储到数据库 with a timestamp
            cursor.execute("INSERT INTO items (title, link, timestamp) VALUES (?, ?, CURRENT_TIMESTAMP)", (data_title, data_link))
            conn.commit()
    return data_list

# 推送函数
def push_message(title, content):
    config = load_config()
    push_config = config.get('push', {})
    
    # 钉钉推送
    if 'dingding' in push_config and push_config['dingding'].get('switch', '') == "ON":
        send_dingding_msg(push_config['dingding'].get('webhook'), push_config['dingding'].get('secret_key'), title,
                          content)

    # 飞书推送
    if 'feishu' in push_config and push_config['feishu'].get('switch', '') == "ON":
        send_feishu_msg(push_config['feishu'].get('webhook'), title, content)

    # Server酱推送
    if 'server_chan' in push_config and push_config['server_chan'].get('switch', '') == "ON":
        send_server_chan_msg(push_config['server_chan'].get('sckey'), title, content)

    # PushPlus推送
    if 'pushplus' in push_config and push_config['pushplus'].get('switch', '') == "ON":
        send_pushplus_msg(push_config['pushplus'].get('token'), title, content)

    # Telegram Bot推送
    if 'tg_bot' in push_config and push_config['tg_bot'].get('switch', '') == "ON":
        send_tg_bot_msg(push_config['tg_bot'].get('token'), push_config['tg_bot'].get('group_id'), title, content)

# 飞书推送
def send_feishu_msg(webhook, title, content):
    feishu(title, content, webhook)

# Server酱推送
def send_server_chan_msg(sckey, title, content):
    server(title, content, sckey)

# PushPlus推送
def send_pushplus_msg(token, title, content):
    pushplus(title, content, token)

# Telegram Bot推送
def send_tg_bot_msg(token, group_id, title, content):
    tgbot(title, content, token, group_id)

# 钉钉推送
def dingding(text, msg, webhook, secretKey):
    ding = cb.DingtalkChatbot(webhook, secret=secretKey)
    ding.send_text(msg='{}\r\n{}'.format(text, msg), is_at_all=False)

# 飞书推送
def feishu(text, msg, webhook):
    ding = cb.DingtalkChatbot(webhook)
    ding.send_text(msg='{}\r\n{}'.format(text, msg), is_at_all=False)

# 钉钉推送
def send_dingding_msg(webhook, secret_key, title, content):
    dingding(title, content, webhook, secret_key)

# 其他推送函数类似，根据需要添加

# 以下是钉钉推送的实现，其他推送方式类似
def dingding(text, msg, webhook, secretKey):
    ding = cb.DingtalkChatbot(webhook, secret=secretKey)
    ding.send_text(msg='{}\r\n{}'.format(text, msg), is_at_all=False)

# Server酱推送
def server(text, msg, sckey):
    try:
        uri = 'https://sc.ftqq.com/{}.send?text={}&desp={}'.format(sckey, text, msg)  
        requests.get(uri, timeout=10)
    except Exception as e:
        pass


# PushPlus推送
def pushplus(text, msg, token):
    try:
        uri = 'https://www.pushplus.plus/send?token={}&title={}&content={}'.format(token, text, msg) 
        requests.get(uri, timeout=10)
    except Exception as e:
        pass


# Telegram Bot推送
def tgbot(text, msg, token, group_id):
    try:
        bot = telegram.Bot(token='{}'.format(token))  
        bot.send_message(chat_id=group_id, text='{}\r\n{}'.format(text, msg))
    except Exception as e:
        pass

# 判断是否应该sleep
def should_sleep():
    now = datetime.datetime.now().time()
    return now.hour < 7

# 主函数
def main():
    banner = '''\n    +-------------------------------------------+
                   安全社区推送监控
    使用说明：
    1. 修改config.yaml中的推送配置以及开关
    2. 修改rss.yaml中需要增加删除的社区
    3. 可自行去除或增加新的推送渠道代码到本脚本中
                      2023.10.10
                   Powered By：Pings
    +-------------------------------------------+
                     开始监控...
    '''

    print(banner)
    conn = init_database()
    cursor = conn.cursor()
    rss_config = {}

    with open('rss.yaml', 'r', encoding='utf-8') as file:
        rss_config = yaml.load(file, Loader=yaml.FullLoader)

    # 发送启动通知消息
    push_message("安全社区文章监控已启动!", "为了减少内卷，该工具在 00:00 到 07:00 间不会进行推送! \n启动时间：{}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))

    while True:
        if should_sleep():
            time.sleep((7 - datetime.datetime.now().hour) * 3600)
            continue

        try:
            for website, config in rss_config.items():
                website_name = config.get("website_name")
                rss_url = config.get("rss_url")
                check_for_updates(rss_url, website_name, cursor, conn)

            # 每二小时执行一次
            time.sleep(7200)

        except Exception as e:
            print("发生异常：", str(e))
            time.sleep(60)  # 出现异常，等待1分钟继续执行

    conn.close()

if __name__ == "__main__":
    main()