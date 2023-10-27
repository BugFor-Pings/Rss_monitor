# rss_monitor
自写的RSS订阅文章推送程序，支持多个平台推送| Self-written RSS subscription article push program, support multiple platforms push


## 0x01 编写思路

使用rss.yaml文件来存储RSS订阅地址和相关名称。

使用config.yaml来存储推送平台配置以及推送开关等信息

使用SQLite来存储推送过的文章名称，文章链接，以及文章推送的时间

在获取文章的时候，获取文章标题以及文章链接，使用文章链接进行重复检测，对比数据库中存在的链接。如果存在则不推送，如果不存在则记录入库进行推送

编写各平台（钉钉，飞书，Server酱，TG_Bot，Pushplus）推送函数，将获取到的文章按照对应rss订阅名称进行推送  比如：SeeBug 今日更新： 标题：********* 链接：*********** 推送时间：xxxx-xx-xx **：**：**

增加一个监控开启消息推送告知，方便看到程序是否正常运行

最后加个 banner，然后开始测试程序是否正常

---
特别感谢：https://github.com/zhengjim/Chinese-Security-RSS  此项目作者

使用此项目获取到了众多安全社区以及个人博客和众多的安全公众号的订阅地址，虽然不认识这个项目的作者，在这里还是感谢这位大佬的项目

在此也特别感谢：程皮糖别皮师傅，对我的代码进行整理修复，解决了重复推送等相关问题。

---
## 0x02 安装与使用

1.先使用pip安装所需要用到的依赖裤

```
pip install -r requirements.txt
```

2.随后修改rss.yaml文件中所需要监控的订阅地址

![img](https://mmbiz.qpic.cn/mmbiz_jpg/WqibHnoQAhZfsQbNu18WVZq52MFWZneZkInXJowZvPPMd6fehoxsIeuvpdazg5QpwK1icdEE7kkVwdDE3EsMsRsg/640?wx_fmt=jpeg&wxfrom=13&tp=wxpic)

3.以及修改config.yaml中的相关推送配置

![](https://mmbiz.qpic.cn/mmbiz_jpg/WqibHnoQAhZfsQbNu18WVZq52MFWZneZk1ticib6YscmiapaJDjefQExxjmOMhEQhJlYOJlUTYNbdXyps6tVLvUZRw/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

4.最后直接运行sec_monitor.py即可，运行效果图如下。

```
python sec_monitor.py
```

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/WqibHnoQAhZfsQbNu18WVZq52MFWZneZkxdibOkr4ZQtPfibhUO1UjOf9Fk6scb6MB93ws1GnWeW7ice2ticCNIQX8w/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

运行程序之后会生成articles.db数据库文件用来存储推送过的文章。

#  

当然这个RSS订阅多渠道推送程序不止用来推送安全社区的文章，反正用处很多，自寻研究吧，觉得该项目不错的话，麻烦给一个star或者fork到自己仓库进行二开

2023-10.31 By:Pings

