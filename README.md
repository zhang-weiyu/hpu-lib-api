<h1 style="text-align: center">HPU图书馆座位编号与API收集整理</h1>

<h3 style="text-align: center">野生API文档</h3>

- [一、前言](#一前言)
- [二、过程](#二过程)
- [三、接口](#三接口)
  - [登陆](#登陆)
  - [用户信息](#用户信息)
  - [历史预约记录](#历史预约记录)
  - [违约记录](#违约记录这个我不太清楚我没有违约记录)
  - [当前预约信息](#当前预约信息)
  - [预约](#预约)
  - [各个图书馆各楼层概况](#各个图书馆各楼层概况)
  - [可用座位查询](#可用座位查询)

## 一、前言

本来是为了考试周抢座用的，后来懒得管了，最近看了看，座位 ID 已经变了，看有没有时间从新看看吧。

## 二、过程

使用手机端，`Packet Capture`软件进行抓包。

## 三、接口

### 登陆

> http://seatlib.hpu.edu.cn/rest/auth?username=&password=

_请求方式：GET_

**url 参数：**

| 参数名   | 类型 | 内容 | 必要性 |
| -------- | ---- | ---- | ------ |
| username | str  | 学号 | 必要   |
| password | str  | 密码 | 必要   |

**json 回复：**

| 字段    | 类型 | 内容         | 备注             |
| ------- | ---- | ------------ | ---------------- |
| status  | str  | 登陆是否成功 | success：成功    |
| data    | obj  | 返回内容     | 失败时返回 null  |
| code    | str  | 状态码       | 成功时应该时是 0 |
| message | str  | 信息         | 成功时应该是空   |

`data`对象：

| 字段  | 类型 | 内容  | 备注           |
| ----- | ---- | ----- | -------------- |
| token | str  | token | 登陆成功时返回 |

### 用户信息

> http://seatlib.hpu.edu.cn/rest/v2/user?token=

_请求方式：GET_

**url 参数：**

| 参数名 | 类型 | 内容  | 必要性 |
| ------ | ---- | ----- | ------ |
| token  | str  | token | 必要   |

**json 回复：**

| 字段    | 类型 | 内容     | 备注             |
| ------- | ---- | -------- | ---------------- |
| status  | str  | 是否成功 | success：成功    |
| data    | obj  | 返回内容 | 失败时返回 null  |
| code    | str  | 状态码   | 成功时应该时是 0 |
| message | str  | 信息     | 成功时应该是空   |

`data`对象：

| 字段           | 类型 | 内容                 | 备注 |
| -------------- | ---- | -------------------- | ---- |
| id             | num  | 未知                 |      |
| enable         | bool | 未知                 |      |
| username       | str  | 学号                 |      |
| status         | str  | 未知                 |      |
| lastLogin      | str  | 上次登陆时间         |      |
| checkdIn       | bool | 未知(应该是是否签到) |      |
| violationCount | num  | 违约记录数           |      |

### 历史预约记录

> http://seatlib.hpu.edu.cn/rest/v2/history/params1/params2?token=

_请求方式：GET_

**url 路径：**

| 参数名  | 内容          | 必要性 |
| ------- | ------------- | ------ |
| params1 | 第 x 页       | 不确定 |
| params2 | 每页显示 x 条 | 不确定 |

> 例：http://seatlib.hpu.edu.cn/rest/v2/history/1/10?token=
> 以每页十条历史记录，显示第一页

**url 参数：**

| 参数名 | 类型 | 内容  | 必要性 |
| ------ | ---- | ----- | ------ |
| token  | str  | token | 必要   |

**json 回复：**

| 字段    | 类型 | 内容     | 备注             |
| ------- | ---- | -------- | ---------------- |
| status  | str  | 是否成功 | success：成功    |
| data    | obj  | 返回内容 | 失败时返回 null  |
| code    | str  | 状态码   | 成功时应该时是 0 |
| message | str  | 信息     | 成功时应该是空   |

`data`对象：

| 字段         | 类型  | 内容             | 备注 |
| ------------ | ----- | ---------------- | ---- |
| reservations | array | 预约历史记录列表 |      |

### 违约记录

> http://seatlib.hpu.edu.cn/rest/v2/violations?token=

_请求方式：GET_

**url 参数：**

| 参数名 | 类型 | 内容  | 必要性 |
| ------ | ---- | ----- | ------ |
| token  | str  | token | 必要   |

**json 回复：**

| 字段   | 类型  | 内容     | 备注            |
| ------ | ----- | -------- | --------------- |
| status | str   | 是否成功 | success：成功   |
| data   | array | 返回内容 | 失败时返回 null |

### 当前预约信息

> http://seatlib.hpu.edu.cn/rest/v2/user/reservations?token=

_请求方式：GET_

**url 参数：**

| 参数名 | 类型 | 内容  | 必要性 |
| ------ | ---- | ----- | ------ |
| token  | str  | token | 必要   |

**json 回复：**

| 字段    | 类型  | 内容     | 备注             |
| ------- | ----- | -------- | ---------------- |
| status  | str   | 是否成功 | success：成功    |
| data    | array | 返回内容 | 失败时返回 null  |
| code    | str   | 状态码   | 成功时应该时是 0 |
| message | str   | 信息     | 成功时应该是空   |

`data`数组中仅含有一个对象，该对象内容：

| 字段      | 类型 | 内容         | 备注                                               |
| --------- | ---- | ------------ | -------------------------------------------------- |
| id        | num  | 未知         |                                                    |
| receipt   | str  | 未知         |                                                    |
| onDate    | str  | 预约日期     |                                                    |
| seatID    | num  | 座位 ID      |                                                    |
| status    | str  | 状态         |                                                    |
| location  | str  | 座位详细位置 | 如南校区第二图书馆 7 层 7 层北部阅览区，座位号 xxx |
| begin     | str  | 开始时间     |                                                    |
| end       | str  | 结束时间     |                                                    |
| userEnded | bool |              |                                                    |
| message   | str  | 信息         |                                                    |

### 预约

> http://seatlib.hpu.edu.cn/rest/v2/freeBook

_请求方式：POST_

**正文参数（ application/x-www-form-urlencoded ）：**

| 参数名    | 类型 | 内容            | 必要性 | 备注                                                  |
| --------- | ---- | --------------- | ------ | ----------------------------------------------------- |
| token     | str  | token           | 必要   | 从登陆接口获取                                        |
| seat      | num  | 座位 ID(seatID) | 必要   | 见[座位 ID 表(只包括新图书馆)](新图书馆座位编号.json) |
| startTime | str  | 起始时间        | 必要   | 按分钟计算，如上午 9 点为 540，下午 18 点为 1080      |
| endTime   | str  | 结束时间        | 必要   | 按分钟计算，如上午 9 点为 540，下午 18 点为 1080      |
| date      | str  | 预约日期        | 必要   | 格式为 1970-01-01                                     |

### 各个图书馆各楼层概况

> http://seatlib.hpu.edu.cn/rest/v2/room/stats2/params1/params2?token=

_请求方式：GET_

**url 路径：**

| 参数名  | 内容                | 必要性 |
| ------- | ------------------- | ------ |
| params1 | 图书馆编号          | 必要   |
| params2 | 日期，如 2021-06-07 | 必要   |

> 例：http://seatlib.hpu.edu.cn/rest/v2/room/stats/3/2021-06-07?token=
> 查看南校区第二图书馆各楼层概况

**url 参数：**

| 参数名 | 类型 | 内容  | 必要性 |
| ------ | ---- | ----- | ------ |
| token  | str  | token | 必要   |

**json 回复：**

| 字段    | 类型  | 内容     | 备注             |
| ------- | ----- | -------- | ---------------- |
| status  | str   | 是否成功 | success：成功    |
| data    | array | 返回内容 | 失败时返回 null  |
| code    | str   | 状态码   | 成功时应该时是 0 |
| message | str   | 信息     | 成功时应该是空   |

`data`数组中含有若干个对象(字典)，每个对象(字典)内容一致：

| 字段       | 类型 | 内容               | 备注                                               |
| ---------- | ---- | ------------------ | -------------------------------------------------- |
| roomId     | num  | 房间 ID            | 如南二馆 7 层自主学习空间(Ⅳ)的 ID 为 31            |
| room       | str  | 房间名称           | 如 7 层自主学习空间(Ⅳ)                             |
| floor      | num  | 房间所在楼层       |                                                    |
| maxHour    | num  | 未知               |                                                    |
| reserved   | num  | 推测是已预约座位数 |                                                    |
| inUse      | num  | 推测是在使用座位数 | 如南校区第二图书馆 7 层 7 层北部阅览区，座位号 xxx |
| away       | num  | 推测是暂离座位数   |                                                    |
| totalSeats | num  | 该房间总座位数     |                                                    |
| free       | num  | 推测是空闲座位数   |                                                    |

### 可用座位查询

> http://seatlib.hpu.edu.cn/rest/v2/searchSeats/params1/params2/params3?token=&roomId=&batch=1000&page=1

_请求方式：GET_

**url 路径：**

| 参数名  | 内容                                                      | 必要性 |
| ------- | --------------------------------------------------------- | ------ |
| params1 | 日期，如 2021-06-07                                       | 必要   |
| params2 | 起始时间，以分钟为单位，如 8 点为 480，若选择`现在`则为-1 | 必要   |
| params2 | 结束时间，以分钟为单位，如 12 点为 720                    | 必要   |

> 例：http://seatlib.hpu.edu.cn/rest/v2/searchSeats/2021-06-07/-1/720?token=&roomId=31&batch=1000&page=1
> 查询 2021 年 6 月 7 日 31 号房间(南二馆 7 层自主学习空间(Ⅳ))从现在到 12 点可用座位

**url 参数：**

| 参数名 | 类型 | 内容     | 必要性 |
| ------ | ---- | -------- | ------ |
| token  | str  | token    | 必要   |
| roomId | str  | 房间编号 | 必要   |

**json 回复：**

| 字段   | 类型 | 内容                | 备注            |
| ------ | ---- | ------------------- | --------------- |
| status | bool | 未知，我看到了 true |                 |
| data   | obj  | 返回内容            | 失败时返回 null |

`data`对象中含有 3 个内容：

| 字段    | 类型 | 内容             | 备注 |
| ------- | ---- | ---------------- | ---- |
| seats   | obj  | 座位情况         |      |
| page    | num  | 不明，应该是页数 |      |
| hasMore | bool | 不明             |      |
