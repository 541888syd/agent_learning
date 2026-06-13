# Day 7 笔记：通讯录管理系统（第1周综合项目·完结）

> 日期：2026-06-13 | 状态：完成 ✅

---

## 一、`isdigit()` — 判断字符串是否纯数字

```python
"13800138000".isdigit()    # True  全是数字
"138x".isdigit()           # False 含非数字字符
"".isdigit()               # False 空字符串也返回 False
```

---

## 二、break 只管最近那一层循环

```python
while True:                   # 外层
    for item in items:        # 内层
        if 条件:
            break             # ← 跳出 for，不是跳出 while！
    # break 之后从这继续
```

解决多层循环中的跳转问题：用**标记变量（flag）**配合 `continue`：

```python
found = False
for item in items:
    if 匹配:
        found = True
        break

if found:
    continue      # 跳过本轮外层循环
```

---

## 三、逻辑运算符 and / or（不是 `|` / `&`）

```python
# ❌ | 是位运算符（按位或）
if a | b:

# ✅ and / or 是逻辑运算
if phone.isdigit() and len(phone) == 11:
```

---

## 四、模糊搜索——`in` 用在字符串上

```python
# 列表里找元素
"苹果" in ["苹果", "香蕉"]              # True

# 字符串里找子串（同一个 in）
"张" in "张三"                          # True
"张" in "张三丰"                        # True
"李" in "张三"                          # False
"138" in "13800138000"                 # True
```

---

## 五、`json.dump()` 中 `ensure_ascii` 参数

```python
ensure_ascii=True   # 默认→中文变 \u5f20\u4e09 乱码
ensure_ascii=False  # 正确→中文正常显示
```

---

## 六、嵌套 while True 控制流

通讯录添加功能的完整控制流：

```python
def add_contacts():
    while True:                    # ① 主循环：连续添加多人
        while True:                # ② 姓名循环：重名重输
            # 重名检查
            if 通过:
                break
        while True:                # ③ 电话循环：格式错重输
            # 格式检查
            if 通过:
                break
        # 添加到列表
        if 不想继续:
            break                  # 退出 ①
```

---

## 七、函数式项目结构

```
1. import
2. 读取函数（load）
3. 保存函数（save）
4. 各功能函数（查看/添加/搜索/修改/删除/统计）
5. 主程序：加载数据 → 主循环调度 → 保存退出
```

---

## 八、易错清单

| 错误 | 原因 | 正确 |
|------|------|------|
| `if a \| b:` | `\|` 是位运算不是逻辑或 | `if a or b:` |
| `break` 想退出外层 | break 只管最近一层 | 标记变量 + continue |
| `ensure_ascii=True` | 中文变 Unicode 编码 | `ensure_ascii=False` |
| `for...else` | for 后 else 没 break 就执行 | 注意缩进层级 |
| 索引只查上限不查下限 | 输入 0 能过第 0 个 | `1 <= n <= len` |

---

## ✅ 第 1 周技能全景图

```
print → input → f-string → int/float/str
    ↓
if/elif/else → == != > < → while → break/continue
    ↓
列表[] → append/pop/len → for/range → max/min/sum
    ↓
字典{} → get/del/items → 字典列表 [{},{},{}]
    ↓
def 函数(参数) → return → global → try/except
    ↓
with open() → json.dump/load → os.path.exists → isdigit()
    ↓
🎉 通讯录管理系统（150+ 行）
```
