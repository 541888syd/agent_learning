# Day 4 笔记：字典

---

## 1. 为什么需要字典

列表按位置找：`fruits[0]` → 你要记住"苹果在第0个"
字典按键名找：`student["name"]` → 你要什么直接叫名字

两列表配对的痛点 → 字典一个搞定：

```python
# ❌ 两个列表（容易对不齐）
names = ["小明", "小红"]
scores = [85, 90]

# ✅ 字典（绑在一起）
students = {"小明": 85, "小红": 90}
```

---

## 2. 字典基本语法

```python
d = {"name": "小明", "age": 18, "score": 85}
#     键      值      键    值    键      值
```

---

## 3. 常用操作

| 操作 | 代码 | 说明 |
|------|------|------|
| 取值（安全） | `d.get("name")` | 找不到返回 None，不报错 |
| 取值（直接） | `d["name"]` | 找不到就💥报错 |
| 带默认值 | `d.get("height", 170)` | 找不到就用 170 |
| 加/改 | `d["score"] = 90` | 键存在就改，不存在就加 |
| 删除 | `del d["age"]` | 删掉这个键值对 |
| 删+取 | `d.pop("age")` | 删掉并返回被删的值 |
| 查存在 | `"name" in d` | True/False |
| 个数 | `len(d)` | 几个键值对 |

---

## 4. 遍历的三种方式

```python
d = {"name": "小明", "age": 18}

for k in d:                     # name  age
    print(k)

for v in d.values():            # 小明  18
    print(v)

for k, v in d.items():          # name→小明  age→18
    print(f"{k} → {v}")
```

---

## 5. 字典列表（最常用组合）

```python
todos = [
    {"任务": "买菜", "等级": "高", "完成情况": "未完成"},
    {"任务": "写作业", "等级": "中", "完成情况": "未完成"},
]

# 访问
print(todos[0]["任务"])          # 买菜

# 修改
todos[1]["完成情况"] = "已完成"

# 遍历
for task in todos:
    print(f'{task["任务"]}：{task["完成情况"]}')
```

---

## 6. 列表 vs 字典 vs 字典列表

| | `[]` 列表 | `{}` 字典 | `[{}, {}]` 字典列表 |
|---|----------|----------|-------------------|
| 示例 | `[1, 2, 3]` | `{"a": 1}` | `[{"a":1}, {"b":2}]` |
| 怎么找 | 索引 0, 1, 2 | 键 "a", "b" | 索引拿字典，键拿值 |
| 适合 | 一堆同类型 | 一个有标签的数据 | 多个人/多条记录 |

---

## 7. f-string 中引号冲突

```python
# ❌ 报错：里外都用双引号
print(f"{task["序号"]}")

# ✅ 外面用单引号
print(f'{task["序号"]}')

# ✅ 先取出来
num = task["序号"]
print(f"{num}")
```

---

## 8. 常见坑

| 坑 | 正确做法 |
|----|----------|
| `pop(值)` 而不是 `pop(索引)` | `pop()` 的参数永远是整数索引 |
| `f"{d["key"]}"` 引号冲突 | 外面用单引号 |
| `"str" in [{...}]` 找不到 | 字典列表不能直接用 `in` 查值，要遍历 |
| `max(空列表)` 崩溃 | 先判空 |

---

## 9. 练习参考答案

```python
todos = []

while True:
    num = int(input("\n1.查看 2.添加 3.完成 4.删除 5.排序 6.退出\n选择："))

    if num == 1:
        if not todos:
            print("暂无事项")
        else:
            for task in todos:
                print(f'{task["序号"]}.{task["任务"]}：{task["完成情况"]} {task["等级"]}')

    elif num == 2:
        while True:
            task_num = str(len(todos) + 1)
            name = input("任务名称：")
            level = input("等级（高/中/低）：")
            todos.append({"序号": task_num, "任务": name, "等级": level, "完成情况": "未完成"})
            if input("继续？(1继续/2退出)：") != "1":
                break

    elif num == 3:
        if not todos:
            print("暂无任务")
        else:
            name = input("完成任务名称：")
            found = False
            for task in todos:
                if task["任务"] == name:
                    task["完成情况"] = "已完成"
                    found = True
                    print(f"✅ {name} 已完成")
            if not found:
                print("没找到这个任务")

    elif num == 4:
        if not todos:
            print("暂无任务")
        else:
            for i in range(len(todos)):
                print(f'{i+1}. {todos[i]["任务"]}')
            n = int(input("删除第几个："))
            if 1 <= n <= len(todos):
                done = todos.pop(n - 1)
                print(f'✅ 已删除：{done["任务"]}')
            else:
                print("序号不存在！")

    elif num == 5:
        if not todos:
            print("暂无任务")
        else:
            high, mid, low = [], [], []
            for task in todos:
                if task["等级"] == "高":
                    high.append(task)
                elif task["等级"] == "中":
                    mid.append(task)
                else:
                    low.append(task)
            todos.clear()
            todos.extend(high + mid + low)
            for task in todos:
                print(f'{task["序号"]}.{task["任务"]}：{task["完成情况"]} {task["等级"]}')

    elif num == 6:
        print("拜拜")
        break
```

---

## ✅ Day 4 检查清单

- [ ] 理解字典 = 键值对
- [ ] 会用 get / [] / del / pop / in / len
- [ ] 会遍历字典（keys / values / items）
- [ ] 会用字典列表（列表里装字典）
- [ ] 会按某个键排序/分类
- [ ] 知道 f-string 引号冲突怎么处理
- [ ] 独立完成待办事项字典升级版
