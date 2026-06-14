# Day 7 笔记：通讯录管理系统（第1周综合项目·完结）

> 日期：2026-06-13 | 状态：通关 ✅ | 代码：150+ 行

---

## 一、项目需求

7 功能通讯录，数据存 JSON，关闭重开数据还在。

| 序号 | 功能 | 函数 |
|:---:|------|------|
| 1 | 查看所有 | `show_contacts()` |
| 2 | 添加 | `add_contacts()` |
| 3 | 搜索 | `search_contact()` |
| 4 | 修改 | `edit_contact()` |
| 5 | 删除 | `delete_contact()` |
| 6 | 统计 | `show_stats()` |
| 7 | 保存退出 | `save_contacts()` |

---

## 二、程序结构（标准模板）

```python
import os
import json

# 1. 加载函数
def contacts_read():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# 2. 保存函数
def save_contacts():
    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=2)

# 3~8. 功能函数（查看/添加/搜索/修改/删除/统计）

# 9. 主程序
contacts = contacts_read()
while True:
    function = input("1.查看 2.添加 ... 7.退出：")
    if function == "1":
        show_contacts()
    ...
    elif function == "7":
        save_contacts()
        break
```

---

## 三、Day 7 新知识点

### 1. `isdigit()` — 判断纯数字

```python
"13800138000".isdigit()    # True
"138x".isdigit()           # False
"".isdigit()               # False
```

### 2. `break` 只管最近一层循环

```python
while True:                    # 外层
    for item in items:         # 内层
        if 条件:
            break              # ← 跳出 for，不是 while！
```

解决方案：**标记变量 + continue**

```python
while True:
    found = False
    for item in items:
        if 条件:
            found = True
            break
    if found:
        continue              # 跳过本轮外层
    # 没找到才继续
```

### 3. 模糊搜索：`in` 用于字符串

```python
"张" in "张三"               # True
"138" in "13800138000"       # True
"李" in "张三"               # False
```

### 4. 逻辑运算符 `and` / `or`

```python
# ❌ | 是位运算（不是逻辑或）
if a | b:

# ✅ 逻辑运算
if phone.isdigit() and len(phone) == 11:
```

---

## 四、第 1 周全部技能清单

### Python 语法基础

| 知识点 | 例子 |
|--------|------|
| `print()` | `print("你好")` |
| 变量 | `name = "小明"` |
| `input()` | `name = input("姓名：")` |
| f-string | `print(f"你好{name}")` |
| `int()` / `str()` / `float()` | `int(input("年龄："))` |
| `type()` | `type(25)` → int |
| 注释 | `# 单行` / `"""多行"""` |

### 判断与循环

| 知识点 | 例子 |
|--------|------|
| `if/elif/else` | `if score >= 90: ... elif score >= 70:` |
| 比较 `== != > < >= <=` | `if name == "小明":` |
| `while` | `while count < 5:` |
| `break` | 跳出循环 |
| `continue` | 跳过本轮 |
| `import random` | `random.randint(1, 100)` |
| 缩进规则 | 同级代码缩进一致 |

### 列表

| 知识点 | 例子 |
|--------|------|
| 创建 | `fruits = ["苹果", "香蕉"]` |
| `append(x)` | 末尾添加 |
| `pop(i)` | 按索引删除 |
| `remove(x)` | 按值删（有坑，重复时只删第一个） |
| `len(list)` | 个数 |
| `in` | `"苹果" in fruits` |
| `if not list:` | 空列表判断 |
| `for item in list:` | 遍历 |
| `for i in range(len(list)):` | 带编号遍历 |
| `range(n)` | 0 到 n-1 |
| `max()` / `min()` / `sum()` | 最大/最小/求和 |
| `enumerate(list, start)` | 自动编号遍历 |

### 字典

| 知识点 | 例子 |
|--------|------|
| 创建 | `d = {"姓名": "张三", "年龄": 25}` |
| 取值 | `d["姓名"]` 或 `d.get("姓名")` |
| 加/改 | `d["性别"] = "男"` |
| 删 | `del d["年龄"]` 或 `d.pop("年龄")` |
| `in` | `"姓名" in d` |
| `.keys()` | 所有键 |
| `.values()` | 所有值 |
| `.items()` | 键值对遍历 |
| 字典列表 | `[{"姓名":"张三"}, {"姓名":"李四"}]` |

### 函数

| 知识点 | 例子 |
|--------|------|
| 定义 | `def add(a, b):` |
| 参数 | `def greet(name):` |
| 返回 | `return result` |
| 全局变量 | 有 `=` 才需要 `global` |
| `enumerate` | `for i, item in enumerate(list, 1):` |
| `try/except` | 防崩溃 |

### 文件与 JSON

| 知识点 | 例子 |
|--------|------|
| `open(file, mode, encoding)` | 打开文件 |
| 三种模式 `r`/`w`/`a` | 读/写/追加 |
| `with ... as f:` | 自动关门 |
| `f.read()` | 读内容 |
| `f.write(s)` | 写字符串 |
| `json.dump(obj, f)` | Python → JSON 文件 |
| `json.load(f)` | JSON 文件 → Python |
| `json.dumps(obj)` | Python → JSON 字符串 |
| `json.loads(s)` | JSON 字符串 → Python |
| `ensure_ascii=False` | 中文正常 |
| `os.path.exists(file)` | 文件存在？ |
| 路径反斜杠坑 | `\\` 或 `r""` 或 `/` |

---

## 五、易错点汇总

| 错误 | 正确 |
|------|------|
| `if a \| b:` | `if a or b:` |
| `break` 想跳出外层 | 标记变量 + `continue` |
| `ensure_ascii=True`（默认） | `ensure_ascii=False` |
| `f.write(list)` 崩溃 | 用 `json.dump()` |
| 路径 `C:\Users` 反斜杠 | `C:/Users` 或 `C:\\Users` |
| 读和写用不同文件名 | 统一文件名 |
| `json.loads(f)` 文件当字符串 | 文件用 `json.load(f)` |
| 索引不查下限 | `1 <= n <= len(list)` |
