# GoAgent Monitor

这个项目是为一个 V2EX 上的帖子而生：

[《请问有人可以提供一个搭建在openshift(或者其他免费云平台)上的一个监测gae appid是否超出配额的源代码么？(供公共goagent服务端使用)》](http://www.v2ex.com/t/68495)


## 功能

这是一个搭建在 GAE 上的爬虫程序。

它监视一个 Appid 列表，这些 Appid 上面都部署了 GoAgent。本程序可返回 JSON 格式的数据，包括：

1. 限额已经用完 的 Appid 列表
2. 仍然可用的 Appid 列表
3. 当前所用流量和每日流量重置之前所消耗的流量
