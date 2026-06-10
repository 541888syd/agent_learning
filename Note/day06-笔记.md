# Day 6 笔记：文件读写 + JSON 持久化

> 日期：2026-06-10 | 任务：待办事项数据存到文件，关掉程序再开数据还在

---

## 一、为什么要文件读写

程序里的变量（如 `todos = []`）存在内存里，程序一关就没了。
文件读写把数据存到硬盘上，关机也不丢。

---

## 二、打开文件 `open()`

```python
f = open("文件名", "模式", encoding="utf-8")
```

| 参数 | 意思 |
|------|------|
| `"文件名"` | 要操作的文件，不写路径就在当前目录 |
| `"模式"` | `"r"` 读 / `"w"` 写 / `"a"` 追加 |
| `encoding="utf-8"` | 编码，写中文必须加 |

---

## 三、三种模式

| 模式 | 能读 | 能写 | 文件不存在 | 文件存在 |
|------|:---:|:---:|------|------|
| `"r"` | ✅ | ❌ | 💥报错 | 从开头读 |
| `"w"` | ❌ | ✅ | 新建 | **先清空**再写 |
| `"a"` | ❌ | ✅ | 新建 | 追加在末尾 |

---

## 四、路径的坑

```python
# ❌ 反斜杠是转义符，\U \6 被当成特殊符号
open("C:\Users\syd\Desktop\666.txt")

# ✅ 三种写法
open("C:\\Users\\syd\\Desktop\\666.txt")    # 双反斜杠
open(r"C:\Users\syd\Desktop\666.txt")       # 前面加 r（raw）
open("C:/Users/syd/Desktop/666.txt")        # 正斜杠，推荐
```

---

## 五、读文件

```python
# 手写版
f = open("test.txt", "r", encoding="utf-8")
content = f.read()    # 把整个文件读成一个字符串
f.close()             # 必须关

# with 版（推荐，自动关门）
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

`"r"` 是说"我要读"，`f.read()` 才是真正去读内容。

---

## 六、写文件

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
```

`f.write()` 只接受字符串，不能直接传列表或字典。

---

## 七、JSON 存储

### 为什么不用 `str(todos)`？

`str()` 糊弄写进去，下次读回来不是标准格式，解析不了。

### 写入：`json.dump()`

```python
import json

with open("todos.json", "w", encoding="utf-8") as f:
    json.dump(todos, f, ensure_ascii=False, indent=2)
```

| 参数 | 意思 |
|------|------|
| `todos` | 要存的 Python 数据 |
| `f` | 写进哪个文件 |
| `ensure_ascii=False` | 不加的话中文变 `\u5c0f\u660e` |
| `indent=2` | 缩进 2 格，排版好看 |

### 读取：`json.load()`

```python
with open("todos.json", "r", encoding="utf-8") as f:
    todos = json.load(f)
```

从 JSON 文件读回 Python 的列表/字典，跟没存过一样用。

---

## 八、文件不存在的处理

```python
import os

if os.path.exists("todos.json"):
    # 文件存在 → 加载
    with open("todos.json", "r", encoding="utf-8") as f:
        todos = json.load(f)
else:
    # 第一次运行 → 空列表起步
    todos = []
```

`os.path.exists("文件名")` 检查文件在不在，存在返回 `True`。

写成函数更干净：

```python
def load_todos():
    if os.path.exists("todos.json"):
        with open("todos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []
```

---

## 九、完整流程

```
程序启动 → load_todos() → 有文件就加载，没有就空列表
    ↓
主循环（跟之前一样）
    ↓
每次增/删/改 → json_write() → 立马存到文件
    ↓
退出
```

---

## 十、易错点

| 错误 | 原因 | 正确 |
|------|------|------|
| 路径反斜杠报错 | `\` 是转义符 | 双写 `\\` 或加 `r` 或用 `/` |
| `f.write(列表)` 报错 | write 只认字符串 | 用 `json.dump()` |
| `"w"` 读不了 | 模式定了权限 | `"w"` 只写，`"r"` 只读 |
| 读和写用了不同文件名 | 比如 `todos.json` vs `dodos.json` | 统一用一个名字 |
| 忘了调 `save_todos()` | 改了数据没存 | 增/删/改后都调一次 |

---

## 十一、常用函数速查

| 函数 | 作用 |
|------|------|
| `open(file, mode, encoding)` | 打开文件 |
| `f.read()` | 读全部内容 |
| `f.write(str)` | 写字符串 |
| `json.dump(obj, f, ...)` | Python→JSON 写入文件 |
| `json.load(f)` | 文件→Python 读取 |
| `os.path.exists(path)` | 检查文件/文件夹是否存在 |

---

## ✅ Day 6 检查清单

- [ ] 理解 `"r"` `"w"` `"a"` 三种模式的区别
- [ ] 会用 `with open()` 读写文件
- [ ] 会用 `json.dump()` 和 `json.load()`
- [ ] 会用 `os.path.exists()` 判断文件存在
- [ ] 知道路径反斜杠的坑
- [ ] 独立完成待办事项的 JSON 持久化
