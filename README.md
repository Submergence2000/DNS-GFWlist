# DNS-GFWlist
尝试通过DNS污染的数据构建DNS污染的GFWlist名单。



## 项目说明

1. 本项目最初只用于《计算机网络课程》的实验，本人严格遵守了《计算机信息网络国际联网安全保护管理办法》相关规定。
2. 因为用了不够高明的请求方法，所以不保证长期的稳定查询，但是项目至少在2020.12.11正常运行。
3. 测试环境为南京大学校园网，但是通过测试发现学校的DNS污染和DNS攻击并不严重，所得结果远远小于GFWlist中的记录。
4. 本次课堂分享的PPT也一并放在本项目的根目录下。
5. 只测试技术，所有内容不掺杂个人情感也不要恶意推断作者立场。



## 使用方法

安装依赖：

```python
pip install -r requirements.txt
```

运行main.py



## 技术实现

### 动机：

1. 如果一直尝试请求[www.google.com](http://www.google.com/)，会发现DNS返回的IP地址有且仅有那几个。

2. 如果反向查询DNS返回的错误的IP地址，我们可以得到其它被污染的网址。（这个仅限于国内的DNS反向查询，国外的DNS反向查询api是没有用的）

### 搜索方法：

首先指定一组初始网址（自选DNS攻击比较严重的），以较大的权值初始化一个字典。

循环若干次：

​	从字典中选取当前权值最大的网址。

​	对该网址进行DNS请求，并进行反查。

​	若该请求确实被攻击，则将反查的所有的网址在字典中的权值加1。

降序返回最后更新过的字典。

### 使用的python包

requests：构造对于在IP138上对于IP反向查询的请求。

beautifulsoup4：对请求的数据进行处理。

dnspython：对网址进行DNS请求

python_Levenshtein：计算请求的域名字符串和通过IP反查得到的域名列表的字符串的编辑距离以筛除未被污染的DNS查询结果。



## 未来可能会做的

1. 对得到的网站进行分类（最新小黄网域名获取？但其实意义不大）

2. 对不同地区，不同运营商的DNS污染情况进行分析。

