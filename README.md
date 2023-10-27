# rss_monitor
自写的RSS订阅文章推送程序，支持多个平台推送| Self-written RSS subscription article push program, support multiple platforms push

项目将于10月31日生日当天进行上传

## 0x01 编写思路

使用rss.yaml文件来存储RSS订阅地址和相关名称。
Use the RSs.yaml file to store RSS subscription addresses and associated names.

使用config.yaml来存储推送平台配置以及推送开关等信息
Use config.yaml to store information such as push platform configuration and push switches

使用SQLite来存储推送过的文章名称，文章链接，以及文章推送的时间
Use SQLite to store the name of the pushed article, the link to the article, and the time the article was pushed

在获取文章的时候，获取文章标题以及文章链接，使用文章链接进行重复检测，对比数据库中存在的链接。如果存在则不推送，如果不存在则记录入库进行推送
When getting articles, get article titles and article links, use article links for repeat detection, and compare links existing in the database. If it exists, it is not pushed. If it does not exist, the record is stored in the database and pushed

编写各平台（钉钉，飞书，Server酱，TG_Bot，Pushplus）推送函数，将获取到的文章按照对应rss订阅名称进行推送  比如：SeeBug 今日更新： 标题：********* 链接：*********** 推送时间：xxxx-xx-xx **：**：**
Write push functions for each platform (Dingbing, Feishu, Server paste, TG_Bot, Pushplus), and push the obtained articles according to the corresponding rss subscription names, such as: SeeBug updated today: Title: ********* Link: *********** Push time: xxxx-xx-xx ** : ** : **

增加一个监控开启消息推送告知，方便看到程序是否正常运行
Add a monitor to enable push notifications to see if the program is running properly

最后加个 banner，然后开始测试程序是否正常
Add a banner at the end and start testing the program to see if it works

---
特别感谢：https://github.com/zhengjim/Chinese-Security-RSS  此项目作者
Special thanks to: https://github.com/zhengjim/Chinese-Security-RSS this project the author

使用此项目获取到了众多安全社区以及个人博客和众多的安全公众号的订阅地址，虽然不认识这个项目的作者，在这里还是感谢这位大佬的项目
Use this project to obtain many security community and personal blog and many security public number subscription address, although I do not know the author of this project, here is still to thank the big guy's project

在此也特别感谢：程皮糖别皮师傅，对我的代码进行整理修复，解决了重复推送等相关问题。
Here also special thanks: Cheng PI sugar PI master, to sort out and repair my code, to solve the repeated push and other related problems.

---
## 0x02 安装与使用

1.先使用pip安装所需要用到的依赖裤
1. First use the dependency pants required for pip installation
```
pip install -r requirements.txt
```

2.随后修改rss.yaml文件中所需要监控的订阅地址
2. Then modify the subscription address that needs to be monitored in the rss.yaml file

![img](https://mmbiz.qpic.cn/mmbiz_jpg/WqibHnoQAhZfsQbNu18WVZq52MFWZneZkInXJowZvPPMd6fehoxsIeuvpdazg5QpwK1icdEE7kkVwdDE3EsMsRsg/640?wx_fmt=jpeg&wxfrom=13&tp=wxpic)

3.以及修改config.yaml中的相关推送配置
3. And modify the relevant push configuration in config.yaml

![](https://mmbiz.qpic.cn/mmbiz_jpg/WqibHnoQAhZfsQbNu18WVZq52MFWZneZk1ticib6YscmiapaJDjefQExxjmOMhEQhJlYOJlUTYNbdXyps6tVLvUZRw/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

4.最后直接运行sec_monitor.py即可，运行效果图如下。
4. Finally, run sec_monitor.py directly. The running effect is as follows.
```
python sec_monitor.py
```

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/WqibHnoQAhZfsQbNu18WVZq52MFWZneZkxdibOkr4ZQtPfibhUO1UjOf9Fk6scb6MB93ws1GnWeW7ice2ticCNIQX8w/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

运行程序之后会生成articles.db数据库文件用来存储推送过的文章。
After running the program, the articles.db database file is generated to store the pushed articles.

#  
当然这个RSS订阅多渠道推送程序不止用来推送安全社区的文章，反正用处很多，自寻研究吧，觉得该项目不错的话，麻烦给一个star或者fork到自己仓库进行二开
Of course, this RSS subscription multi-channel push program is not only used to push security community articles, anyway, a lot of use, self-search research, think that the project is good, trouble to give a star or fork to their own warehouse for two open
#  
2023-10.31 By:Pings

