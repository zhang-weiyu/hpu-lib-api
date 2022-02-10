# 当前预约信息

> http://seatlib.hpu.edu.cn/rest/v2/user/reservations?token=

*请求方式：GET*

**url 参数：**

| 参数名 | 类型 | 内容  | 必要性 |
| ------ | ---- | ----- | ------ |
| token  | str  | token | 必要   |

**json 回复：**

根对象：

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