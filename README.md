# Python 学习记录

> 大一上的 Python 练习仓库
> 从 `print("hello")` 开始，到能写出一个拆成 4 个文件的命令行工具

---

## 这是什么

不是教程，是我的练习记录。

每个文件对应一个知识点，**编号就是学习顺序**。

其中「待办清单」写了三遍（11 → 12 → 13），每次都是拿新学的东西重写一遍——
同样的需求，不同的工具，这是我觉得最有效的复习方式。

---

## 目录

### 基础语法

| 文件 | 内容 |
|---|---|
| `01_hello.py` | 输出、变量、类型 |
| `02_score.py` | `if / elif / else` |
| `03_sum.py` | `for` 循环、累加器 |

### 文件与字符串

| 文件 | 内容 |
|---|---|
| `04_make_log.py` | 写文件 |
| `05_count_error.py` | 读文件 + 计数（`grep -c` 的 Python 版） |
| `06_guess.py` | `while` + `try/except` |
| `07_split_demo.py` | 字符串切分 |
| `08_dict_practice.py` | 字典计数 |
| `09_log_analysis_if.py` | 日志统计（`if/else` 版） |
| `10_log_analysis_sorted.py` | 日志统计（`.get()` + 排序） |

### 待办清单：三次重构

| 文件 | 内容 |
|---|---|
| `11_todo_v1.py` | 列表套字典 + 四个函数 |
| `12_todo_v2.py` | 加 `json` 持久化 |
| `13_todo_v3.py` | 加命令行参数（`sys.argv`） |

### 面向对象

| 文件 | 内容 |
|---|---|
| `14_class_demo.py` | 类、`__init__`、`self` |
| `15_oop_advanced.py` | 继承、`super()`、方法重写 |

### 标准库

| 文件 | 内容 |
|---|---|
| `17_stdlib_demo.py` | `pathlib`、`datetime` |
| `18_organize.py` | 文件整理器（按后缀归档） |

### 完整版本

| 文件 | 内容 |
|---|---|
| `16_todo_final.py` | 单文件版，153 行，适合从头读到尾 |
| `todo_project/` | 四文件版，真实项目结构 |

---

## 怎么跑

### 环境

- Python 3.13
- 只用了标准库，不需要装第三方包

### 运行单个文件

```bash
python 03_sum.py
```

### 运行完整项目

```bash
cd todo_project

python main.py add 买牛奶
python main.py list
python main.py done 1
python main.py del 2
python main.py clear
```

### 注意

`05`、`09`、`10` 需要 `app.log` 在同目录。
如果丢了，先跑 `04_make_log.py` 重新生成。

`18_organize.py` 会真的移动文件，跑之前确认 `_test_org/` 里只有测试数据。

---

## 学习进度

| 时间 | 内容 |
|---|---|
| 10 月底 | Linux 命令、Git 基础 |
| 11 月初 | Python 语法：变量、判断、循环、函数、文件、异常 |
| 11 月中 | 待办清单 v1 → v2 → v3 |
| 11 月中下 | 面向对象：类、继承 |
| 11 月下旬 | 模块与包、标准库 |
| 进行中 | 正则、虚拟环境、小项目 |

---

## 为什么这么写

**同一个需求写三遍。**

`11` 用字典和函数，`12` 加持久化，`13` 加命令行。

每次重写都能感觉到「上次那样写是因为当时只会那些」。

---

## 说明

代码里有注释，也有踩过坑的痕迹（比如 `self.count += 1` 那个错误写法）。

**留着错误，比只留正确答案更有用。**
