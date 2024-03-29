# Auto-bing-search
简单的自动搜索python脚本，自动在bing上搜索，可模拟移动端搜索，可用于刷搜索次数/Microsoft Reward等

搜索词库来源：[清华大学开放中文词库](http://thuocl.thunlp.org/)

## 如何使用

### 1. 安装[python](https://www.python.org/)环境

### 2. 下载源代码

点击`Code - Download Zip`或者

```shell
git clone https://github.com/ScaredCube/auto-bing-search
```

### 3. 安装依赖库

```shell
pip install requests
```

### 4. 获取cookie

打开[bing主页](https://bing.com)，登录

按`F12`（或者`Fn + F12`）打开开发者工具，选择`Console`（控制台）

在控制台下方输入：`document.cookie`，复制输出的信息（不需要引号）

![img](https://imgs.scc.lol/file/db5c1a156486c23cb4e4c.png)

### 5. 修改账号内容

在cookie.txt中填入bing的cookie，支持多账户，一行一个

在index.py第7行的列表中填入cookie.txt中对应的账号邮箱

例如：

```python
accs=[
    'username1@outlook.com',
    'username2@outlook.com'
]
```

### 6. 运行脚本

双击`index.py`或者

```shell
python index.py
```

### *7. 选择UA

脚本默认使用手机UA用于模拟手机搜索

若想模拟电脑搜索请修改`index.py`第17行UA（19行注释的内容为电脑UA）
