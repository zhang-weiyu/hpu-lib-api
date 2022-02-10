<h1 style="text-align: center">HPU图书馆API收集整理</h1>

<h2 style="text-align: center">其中部分信息可能已经过时失效, 请自己尝试</h2>

## 一、动机

为了考试周的时候占个座位- -

## 二、使用工具

在手机端使用 `Packet Capture` 工具对 `seat` 软件进行抓包获取接口。

## 三、接口内容

- [x] [登录](userInfo/login.md)
- [x] [图书馆公告信息](libInfo/announce.md)
- [x] [用户信息](userInfo)
  - [x] [个人信息](userInfo/userInfo.md)
  - [x] [违约记录](userInfo/violations.md)
  - [x] [历史预约信息](userInfo/history.md)
  - [x] [当前预约信息](userInfo/reservations.md)
- [x] [预约](freeBook/freeBook.md)
- [ ] [信息查询](libInfo)
  - [x] [查询某房间某时间段的可用座位](libInfo/searchSeats.md)
  - [x] [各图书馆各楼层概况](libInfo/roomStats.md)
