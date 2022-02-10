# 各个图书馆各楼层概况

> http://seatlib.hpu.edu.cn/rest/v2/room/stats2/params1/params2?token=

*请求方式：GET*

**url 路径：**

| 参数名  | 内容                | 必要性 |
| ------- | ------------------- | ------ |
| params1 | 图书馆编号          | 必要   |
| params2 | 日期，如 2021-06-07 | 必要   |

**url 参数：**

| 参数名 | 类型 | 内容  | 必要性 |
| ------ | ---- | ----- | ------ |
| token  | str  | token | 必要   |

> 例：http://seatlib.hpu.edu.cn/rest/v2/room/stats/3/2021-06-07?token=
> 查看南校区第二图书馆各楼层概况

**json 回复：**

根对象：

| 字段    | 类型  | 内容     | 备注             |
| ------- | ----- | -------- | ---------------- |
| status  | str   | 是否成功 | success：成功    |
| data    | array | 返回内容 | 失败时返回 null  |
| code    | str   | 状态码   | 成功时应该时是 0 |
| message | str   | 信息     | 成功时应该是空   |

`data`数组中含有若干个对象(字典)，每个对象(字典)内容一致：

| 字段       | 类型 | 内容               | 备注                                    |
| ---------- | ---- | ------------------ | :-------------------------------------- |
| roomId     | num  | 房间 ID            | 如南二馆 7 层自主学习空间(Ⅳ)的 ID 为 31 |
| room       | str  | 房间名称           | 如 7 层自主学习空间(Ⅳ)                  |
| floor      | num  | 房间所在楼层       |                                         |
| maxHour    | num  | 未知               |                                         |
| reserved   | num  | 推测是已预约座位数 |                                         |
| inUse      | num  | 推测是在使用座位数 |                                         |
| away       | num  | 推测是暂离座位数   |                                         |
| totalSeats | num  | 该房间总座位数     |                                         |
| free       | num  | 推测是空闲座位数   |                                         |