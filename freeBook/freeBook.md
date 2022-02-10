# 预约

> http://seatlib.hpu.edu.cn/rest/v2/freeBook

*请求方式：POST*

**正文参数（ application/x-www-form-urlencoded ）：**

| 参数名    | 类型 | 内容            | 必要性 | 备注                                                  |
| --------- | ---- | --------------- | ------ | ----------------------------------------------------- |
| token     | str  | token           | 必要   | 从登陆接口获取                                        |
| seat      | num  | 座位 ID(seatID) | 必要   | 见[座位 ID 表(只包括新图书馆)](新图书馆座位编号.json) |
| startTime | str  | 起始时间        | 必要   | 按分钟计算，如上午 9 点为 540，下午 18 点为 1080      |
| endTime   | str  | 结束时间        | 必要   | 按分钟计算，如上午 9 点为 540，下午 18 点为 1080      |
| date      | str  | 预约日期        | 必要   | 格式为 1970-01-01                                     |