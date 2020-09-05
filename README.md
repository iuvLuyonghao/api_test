RCC接口测试用例库 
=====================

[toc]

## Python版本约束：

仅支持`Python 3.6+`

## 依赖：

### 依赖列表：

版本号仅供参考：

```
Package            Version
------------------ ---------
xeger>=0.3.4
faker==0.8.16
pika==0.12.0
pytest>=3.6.2
qreader==0.3
qav5>=1.0.0
xlrd==1.1.0
elasticsearch>=5.4.0
elasticsearch6
xlwt>=1.2.0
jsonschema>=2.6.0
requests>=2.18.4
pytest-reportportal>=1.0.4
reportportal-client>=3.2.3
aiohttp
arrow
cx-Oracle>=7.2.3
mysql-connector-python>=8.0.18
PyMySQL>=0.9.1
python-json-logger>=0.1.9
simplejson>=3.16.0
redis>=2.10.6
psycopg2>=2.8.4

```

### 依赖安装：

先把`pip.conf`文件拷贝的`$HOME/.pip/`目录下

执行pip命令安装依赖：

```
pip install -r requirements.txt
```

## 执行：

### 执行入口：

```
python runsuite.py
```


### 主要参数：

```
usage: runsuite.py [-h] [--env ENV] [--data-file DATAFILE] [--suites SUITES]

optional arguments:
  -h, --help            show this help message and exit
  --env ENV             用于指定不同的测试环境
  --data-file DATAFILE  用于指定加载额外的测试数据文件,将会覆盖默认的测试数据
  --suites SUITES       用于指定执行哪些目录下的用例（可包含子目录），多个目录用`,`分割, eg: --suites=mega,pangu
```

### pytest执行参数：

请参考`pytest --help`

## 项目文件说明：

```
├── Dockerfile                                      ---------- Dockerfile构建文件
├── README.md   
├── apis                                            ---------- 接口封装目录
│   ├── __init__.py
│   └── mega                                        ---------- mega项目
│       ├── __init__.py
│       └── company                                 ---------- company模块
│           ├── __init__.py
│           └── company.py                          ---------- 接口类文件
├── tests                                           ---------- 测试用例目录
│   ├── __init__.py
│   └── mega                                        ---------- 项目用例目录
│       ├── __init__.py
│       └── company                                 ---------- 模块用例目录
│           ├── __init__.py
│           └── test_company.py                     ---------- 测试用例
├── config.py                                       ---------- 项目配置文件，包含各种服务入口地址、数据源配置信息等
├── conftest.py                                     ---------- pytest fixtures实现
├── const.py                                        ---------- 各种常量，如接口响应码等
├── data                                            ---------- 测试用例数据层
│   ├── __init__.py
│   ├── loader.py                                   ---------- 数据加载函数
│   ├── model.py                                    ---------- 数据用自定义model映射
│   ├── test.json                                   ---------- test环境测试数据
│   └── dev.json                                    ---------- dev环境测试测试数据
├── pip.conf                                        ---------- pip配置文件
├── pytest.ini                                      ---------- pytest配置文件
├── requirements.txt                                ---------- 项目依赖
└── runsuite.py                                     ---------- 测试执行入口
```

