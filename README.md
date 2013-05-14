# GoAgent Monitor

这个项目是为一个 V2EX 上的帖子而生：

[《请问有人可以提供一个搭建在openshift(或者其他免费云平台)上的一个监测gae appid是否超出配额的源代码么？(供公共goagent服务端使用)》](http://www.v2ex.com/t/68495)

使用示例：[https://goagentmonitor.appspot.com/api/wwqgtxx-goagent](https://goagentmonitor.appspot.com/api/wwqgtxx-goagent)

## 功能

这是一个搭建在 GAE 上的爬虫程序。它监视一个 Appid 列表，这些 Appid 上面都部署了 GoAgent。

### 可查询数据

本程序可返回 JSON 格式的数据，包括：

1. 限额已经用完 的 Appid 列表
2. 仍然可用的 Appid 列表
3. 当前所用流量和每日流量重置之前所消耗的流量

格式示例：

    {
      "available": ["wwqgtxxproxy12-4", "wwqgtxxproxy12-5", ...], # 可用的 Appid 列表
      "over_quota": ["wwqgtxxproxy1-1", "wwqgtxxproxy20-10", ...], # 超出配额的 Appid 列表
      "available_str": "今日还剩 153 GB/295 GB 流量"
    }

### 爬虫工作明细

每五分钟抓取一次 fetch_config.py 中定义的各个 URL，并判断 URL 中包涵的 Appids 是否超出配额。

## 如何添加自定义监控列表

在 fetch\_config.py 中，按照示例的格式加进去就好了。查询的时候，用 `cluster_id' 进行查询。如： [https://goagentmonitor.appspot.com/api/wwqgtxx-goagent](https://goagentmonitor.appspot.com/api/wwqgtxx-goagent)

