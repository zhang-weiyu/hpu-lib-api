# 用户个人信息

> http://seatlib.hpu.edu.cn/rest/v2/user?token=

*请求方式：GET*

**url 参数：**

| 参数名 | 类型 | 内容  | 必要性 |
| ------ | ---- | ----- | ------ |
| token  | str  | token | 必要   |

**json 回复：**

根对象：

| 字段    | 类型 | 内容     | 备注                          |
| ------- | ---- | -------- | ----------------------------- |
| status  | str  | 是否成功 | success: 成功<br />fail: 失败 |
| data    | obj  | 返回内容 | 失败时返回 null               |
| code    | str  | 状态码   | 0: 成功<br />10: 系统维护中   |
| message | str  | 信息     | 成功时应该是空                |

`data`对象：

| 字段           | 类型 | 内容         | 备注 |
| -------------- | ---- | ------------ | ---- |
| id             | num  | 未知         |      |
| enable         | bool | 未知         |      |
| username       | str  | 学号         |      |
| status         | str  | 未知         |      |
| lastLogin      | str  | 上次登陆时间 |      |
| checkdIn       | bool | 是否签到     |      |
| violationCount | num  | 违约记录数   |      |