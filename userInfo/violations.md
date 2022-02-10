# 违约记录

> http://seatlib.hpu.edu.cn/rest/v2/violations?token=

*请求方式：GET*

**url 参数：**

| 参数名 | 类型 | 内容  | 必要性 |
| ------ | ---- | ----- | ------ |
| token  | str  | token | 必要   |

**json 回复：**

根对象：

| 字段   | 类型  | 内容     | 备注            |
| ------ | ----- | -------- | --------------- |
| status | str   | 是否成功 | success：成功   |
| data   | array | 返回内容 | 失败时返回 null |
