# 图书馆公告信息

> http://seatlib.hpu.edu.cn/rest/v2/announce

*请求方式: Get*

**json 回复：**

根对象：

| 字段    | 类型 | 内容     | 备注             |
| ------- | ---- | -------- | ---------------- |
| status  | str  | 是否成功 | success：成功    |
| data    | obj  | 返回内容 |                  |
| code    | str  | 状态码   | 成功时应该时是 0 |
| message | str  | 信息     | 成功时应该是空   |