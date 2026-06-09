# Day 5 笔记：Python 函数封装

> 日期：2026-06-09 | 任务：把待办事项程序拆成函数

---

## 一、函数是什么

**把一段代码打包，起个名字，以后用名字调用。**

```python
def 函数名():
    要执行的代码
```

**类比**：遥控器。你按"开机"键，不需要知道里面电路怎么走的。

---

## 二、函数结构（5 部件）

```python
def add_task():                        # ① def + 函数名 + ()
    """添加一条待办事项"""             # ② 文档字符串（说明这函数干嘛的）
    task_name = input("名称：")        # ┐
    todos.append(...)                  # │ ③ 函数体（缩进的所有代码）
    print("已添加")                    # ┘
    # 没有 return                      # ④ 没有 return → 自动返回 None
```

---

## 三、参数

### 3.1 参数就是"函数需要的输入"

```python
def greet(name):            # name 是参数
    print(f"你好，{name}")

greet("小明")               # "小明" 是传入的值
# 输出：你好，小明
```

### 3.2 默认参数

```python
def ask_yes_no(prompt="继续输入：1，结束输入：2 ："):
    return input(prompt) == "1"

ask_yes_no()                        # 不传 → 用默认文字
ask_yes_no("还要加吗？1/2：")       # 传了 → 覆盖默认值
```

**本质**：`prompt` 这个参数被喂给了 `input()`，成了屏幕上的提示文字。

### 3.3 参数类型随意

Python 不检查类型，`: int` 只是给人看的提示：

```python
def add(a: int, b: int) -> int:
    return a + b

add("x", "y")   # 照样跑！类型提示不强制
```

---

## 四、传参的两种方式

### 4.1 位置参数（按顺序）

```python
def order(a, b, c):
    print(a, b, c)

order(1, 2, 3)     # a=1, b=2, c=3  ← 第1个给a，第2个给b，第3个给c
```

### 4.2 关键字参数（按名字）

```python
order(c=3, a=1, b=2)   # 顺序随便，按名字匹配
# 输出：1 2 3
```

### 4.3 有些函数不接受关键字

```python
enumerate(todos, 1)         # ✅ 位置参数
enumerate(todos, start=1)   # 💥 TypeError: enumerate() takes no keyword arguments
```

**记住**：`enumerate(列表, 起始值)` 只能传位置，不能写 `start=`。

### 4.4 有些参数必须用关键字

```python
print("hello", "world", sep="---", end="!!!")
#                         ↑ 必须写名字  ↑ 必须写名字
# 输出：hello---world!!!
```

---

## 五、return（返回值）

### 5.1 有 vs 没有

```python
def 有返回(a, b):
    return a + b

def 没返回():
    print("hello")

x = 有返回(1, 2)   # x = 3
y = 没返回()        # y = None（默认返回空）
```

### 5.2 类型不强制

```python
def get_num() -> int:
    return "不是数字"    # Python 不拦，照常返回字符串
```

---

## 六、作用域（Scope）

### 6.1 核心规则

> 变量在哪里定义，就在哪里能用。函数里的变量外面看不见。

```python
todos = []               # 全局变量，任何地方都能读

def test():
    x = "我在函数里"      # 局部变量，只在这个函数里有效
    print(todos)          # ✅ 能读全局变量

test()
print(x)                 # 💥 NameError！x 已经死了
```

### 6.2 什么时候需要 `global`

**铁律**：变量名左边有 `=`（赋值）就需要 `global`，否则不用。

```python
todos.clear()        # 没 = → 不用 global ✅
todos.append(x)      # 没 = → 不用 global ✅
todos[0] = "新值"    # 没 = → 不用 global ✅    (改的是列表内部)
todos = [1, 2, 3]    # 有 = → 必须 global ⚠️   (整个换了)
todos += [4]         # 有 = → 必须 global ⚠️   (等同于 todos = todos + [4])
```

### 6.3 为什么"修改内容"不需要 global

Python 变量名是**标签**，不是盒子：

```
todos ──────▶ [1, 2, 3]           ← 标签贴在列表上

todos.append(4)                    ← 改了列表本身，标签没动
todos ──────▶ [1, 2, 3, 4]        ← 还是同一个列表

todos = [5, 6]                     ← 把标签撕了，贴到新列表上
todos ──X  [1, 2, 3, 4]
       └──▶ [5, 6]                 ← 需要 global 声明
```

---

## 七、enumerate —— 自动编号

```python
# enumerate(列表, 起始值) → 给每个元素贴序号

list(enumerate(["A", "B", "C"], 1))
# → [(1, "A"), (2, "B"), (3, "C")]
#    序号+元素

# for 循环里用
for i, task in enumerate(todos, 1):
    task["序号"] = str(i)    # i = 1, 2, 3...

# 手写等价于
i = 0
for task in todos:
    i = i + 1
    task["序号"] = str(i)
```

⚠️ **只能传位置参数**：`enumerate(todos, 1)` ✅ / `enumerate(todos, start=1)` ❌

---

## 八、列表拼接 `+`

```python
[1, 2] + [3] + [4, 5]  →  [1, 2, 3, 4, 5]
[] + ["A"] + []         →  ["A"]            # 空列表自动消失

# 应用
for task in high + middle + low:   # 三个列表拼成一个，一次性遍历
    todos.append(task)
```

---

## 九、try/except —— 防崩溃

```python
try:
    num = int(input("输入数字："))
except ValueError:
    print("请输入数字！")    # 用户输 "abc" 也不会崩
```

---

## 十、if __name__ == "__main__"

```python
if __name__ == "__main__":
    main()
```

| 运行方式 | `__name__` | 执行 main 吗 |
|---------|:---:|:---:|
| `python file.py` | `"__main__"` | ✅ 执行 |
| `import file` | `"file"` | ❌ 不执行 |

防止被 import 时自动跑起来。

---

## 十一、Bug 修复记录

| 位置 | 问题 | 修复 |
|------|------|------|
| `finish_task` / `delete_task` | 空列表后还弹"继续吗" | 空时加 `break` 直接退出 |
| `rank_task` | 排序后序号对不上 | `enumerate` 重新编号 |
| `delete_task` / 主循环 | 输字母直接崩溃 | 加 `try/except` |

---

## 十二、最终代码结构

```
todos = []                    ← 全局数据

def ask_yes_no(prompt=...)    ← 工具：问是否继续
def add_task()                ← 添加待办
def show_task()               ← 查看所有
def finish_task()             ← 标记完成
def delete_task()             ← 删除
def rank_task()               ← 排序

主循环                         ← 菜单调度
```
