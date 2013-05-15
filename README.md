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

爬虫会把 URL 中的各个 Appid 加入任务队列等待 GAE 处理，我的任务队列设定是，每秒执行 10 个任务。也就是说，如果你的 GoAgent 集群有 500 个 Appid 的话，需要 50s 来完成更新。

## 如何添加自定义监控列表

监控列表配置文件示例：

    config = {
        # cluster_id
        "wwqgtxx-goagent": {
            "name": u"wwqgtxx-goagent's name", # cluster_name
            "url": "http://goagent.wwqgtxx-goagent.googlecode.com/git/goagent-local/proxy.ini", # get appids from this url
        },
    }

在 fetch\_config.py 中，按照示例的格式加进去就好了。查询的时候，用 `cluster_id' 进行查询。如： [https://goagentmonitor.appspot.com/api/wwqgtxx-goagent](https://goagentmonitor.appspot.com/api/wwqgtxx-goagent)

