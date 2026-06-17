# Day 9 笔记：列表推导式 + 排序 + lambda

> 日期：2026-06-17 | 状态：完成 ✅ | 文件：`Program/day9/main.py`

---

## 一、列表推导式 — 一行生成列表

```python
# ❌ 老写法
result = []
for i in range(5):
    result.append(i * 2)

# ✅ 列表推导式
result = [i * 2 for i in range(5)]      # [0, 2, 4, 6, 8]
```

结构：`[对每项的运算 for 变量 in 可遍历对象]`

### 带条件过滤

```python
[i for i in range(10) if i % 2 == 0]          # 只要偶数 → [0, 2, 4, 6, 8]
[i*2 for i in range(10) if i % 2 == 0]        # 偶数再乘2 → [0, 4, 8, 12, 16]
[name for name in names if name.startswith("张")]  # 只要姓张的
```

---

## 二、`sorted()` — 排序

| 项目 | 内容 |
|------|------|
| **所属库** | 内置（不需要 import） |
| **类型属性** | 序列排序函数 |
| **名字来源** | **sorted** = 排序过的（sort 的过去分词） |
| **功能描述** | 返回排序后的新列表，不修改原列表 |
| **函数签名** | `sorted(iterable, key=None, reverse=False)` |
| **参数列表** | `iterable` — 要排序的东西；`key` — 按什么排序（传函数）；`reverse=True` — 降序 |
| **返回值** | `list` — 排序后的新列表 |

```python
sorted([3, 1, 4, 1, 5])                  # [1, 1, 3, 4, 5]
sorted([3, 1, 4], reverse=True)          # [4, 3, 1]
sorted(["banana", "apple"])              # ['apple', 'banana']
sorted(["aaa", "b", "cc"], key=len)      # ['b', 'cc', 'aaa']  按长度排
```

### `key` 参数 — 告诉它按什么排序

```python
# 按绝对值排
sorted([-5, 3, -1, 4], key=abs)        # [-1, 3, 4, -5]
```

---

## 三、`lambda` — 匿名函数

| 项目 | 内容 |
|------|------|
| **所属库** | Python 关键字（内置） |
| **类型属性** | 函数定义语法 |
| **名字来源** | **lambda** = 希腊字母 λ，数学传统符号表示匿名函数 |
| **功能描述** | 定义一个不需要起名字的短函数，用完就扔 |
| **函数签名** | `lambda 参数: 返回值` |
| **参数列表** | 冒号左边是参数；冒号右边是返回值表达式 |
| **返回值** | 冒号右边表达式的值 |

```python
# 老写法
def get_age(contact):
    return contact["age"]
sorted(list, key=get_age)

# lambda 写法
sorted(list, key=lambda c: c["age"])
```

```python
lambda x: x[1]
#  └─┬─┘  └─┬─┘
#  参数    返回参数的第1号元素
```

---

## 四、主线任务：IP 统计排序

```python
import re

log = """2024-01-01 10:30:45 192.168.1.1 GET /index.html
2024-01-01 10:31:12 10.0.0.5 POST /login
2024-01-01 10:32:01 192.168.1.1 GET /about
2024-01-01 10:33:45 172.16.0.8 GET /contact
2024-01-01 10:34:01 10.0.0.5 GET /about
2024-01-01 10:35:12 10.0.0.5 GET /index.html
2024-01-01 10:36:45 192.168.1.1 POST /login
2024-01-01 10:37:01 172.16.0.8 GET /contact"""

# 1. 正则抓所有IP
contacts = re.findall(r"\d+\.\d+\.\d+\.\d+", log)

# 2. 字典计数
ip_count = {}
for contact in contacts:
    if contact not in ip_count:
        ip_count[contact] = 0       # 首次出现初始0
    ip_count[contact] += 1          # 计数+1

# 3. 按次数排序
ip_sorted = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)

# 4. 输出
for ip, count in ip_sorted:
    print(f"{ip}: {count} 次")
```

### 步骤拆解

1. `re.findall()` → 把所有 IP 捞出来：`['192.168.1.1', '10.0.0.5', ...]`
2. `ip_count` 字典：IP 做键，次数做值
3. `ip_count.items()` → `[("192.168.1.1", 3), ("10.0.0.5", 3), ...]`
4. `lambda x: x[1]` → 按元组第 1 号位置（次数）排序
5. `reverse=True` → 从高到低

---

## 五、挑战：加排名序号

```python
for rank, (ip, count) in enumerate(ip_sorted, 1):
    print(f"第{rank}名: {ip} ({count}次)")
```

`enumerate` 给自动编号；`(ip, count)` 再把元组拆开。
