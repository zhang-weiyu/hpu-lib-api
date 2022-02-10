# seat软件账号密码登录

> <http://seatlib.hpu.edu.cn/rest/auth?username=&password>=

*请求方式：GET*

**url 参数：**

| 参数名   | 类型 | 内容 | 必要性 |
| -------- | ---- | ---- | ------ |
| username | str  | 学号 | 必要   |
| password | str  | 密码 | 必要   |

**json回复：**

根对象：

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
