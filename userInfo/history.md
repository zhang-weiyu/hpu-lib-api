# 历史预约记录

> http://seatlib.hpu.edu.cn/rest/v2/history/params1/params2?token=

*请求方式：GET*

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

根对象：

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