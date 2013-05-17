# GoAgent Monitor

这个项目是为一个 V2EX 上的帖子而生：

[《请问有人可以提供一个搭建在openshift(或者其他免费云平台)上的一个监测gae appid是否超出配额的源代码么？(供公共goagent服务端使用)》](http://www.v2ex.com/t/68495)

使用示例：[https://goagentmonitor.appspot.com/api/wwqgtxx-goagent](https://goagentmonitor.appspot.com/api/wwqgtxx-goagent)

## 功能

这是一个搭建在 GAE 上的爬虫程序。它监视一个 Appid 列表，这些 Appid 上面都部署了 GoAgent。

### 返回的数据格式示例

    {
      "available": ["wwqgtxxproxy12-4", "wwqgtxxproxy12-5", ...], # 可用的 Appid 列表
      "over_quota": ["wwqgtxxproxy1-1", "wwqgtxxproxy20-10", ...], # 超出配额的 Appid 列表
      "status_msg": "今日还剩 207GB/316GB 流量"
    }

### 爬虫工作明细

每 10分钟 抓取一次 fetch_config.py 中定义的各个 URL，并判断 URL 中包涵的 Appids 是否超出配额。

爬虫会把 URL 中的各个 Appid 加入任务队列等待 GAE 处理，我的任务队列设定是，每秒执行 10 个任务。也就是说，如果你的 GoAgent 集群有 500 个 Appid 的话，需要 50s 来完成一次全部抓取。

## FAQ

1. 如何部署一个自己的 monitor 服务？

下载这个 repo 的代码，然后更改 app.yaml 里面的 `application: goagentmonitor` 字段，把 `goagentmonitor` 改成你自己的 Appid。

接着，更改 fetch\_config.py 文件，加入你想监控的 GAE 集群列表。

如果你想马上看到该服务的效果的话，以管理员身份访问一下 /start_fetch 这个地址来触发爬虫。

2. 如何添加自定义监控列表

监控列表配置文件示例：

    config = {
        # cluster_id
        "wwqgtxx-goagent": {
            "name": u"wwqgtxx-goagent's name", # cluster_name
            "url": "http://goagent.wwqgtxx-goagent.googlecode.com/git/goagent-local/proxy.ini", # get appids from this url
        },
    }

在 fetch\_config.py 中，按照示例的格式加进去就好了。查询的时候，用 `cluster_id' 进行查询。如： [https://goagentmonitor.appspot.com/api/wwqgtxx-goagent](https://goagentmonitor.appspot.com/api/wwqgtxx-goagent)


## TODO

1. 缓存 Appid 列表

2. 一个 task 里面抓取多个 Appid 信息

3. 抓取时，放弃已经 503 的 Appid，并每天 flush 一次 memcache

4. 支持更多 Appid 列表文件的格式