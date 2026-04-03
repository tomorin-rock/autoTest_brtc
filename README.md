# BRTC API 自动化测试项目

## 项目简介

这是一个基于 Python + Requests + Pytest + Allure 框架的 BRTC 系统 API 自动化测试项目。项目实现了用户注册、登录、获取用户信息、创建订单等核心功能的自动化测试，并生成美观的 Allure 测试报告。

## 项目结构

```
autoTest_brtcApi/
├── api/                # API 接口类
│   ├── __init__.py
│   └── usermanage.py   # 用户管理相关接口
├── core/               # 核心功能
│   ├── __init__.py
│   └── executeReq.py   # 请求执行模块
├── test_cases/         # 测试用例
│   ├── __init__.py
│   ├── test_01_register.py    # 注册测试
│   ├── test_02_login.py       # 登录测试
│   ├── test_03_getUser.py     # 获取用户信息测试
│   └── test_04_createOrder.py # 创建订单测试
├── utils/              # 工具类
│   ├── __init__.py
│   ├── getPath.py      # 路径工具
│   ├── log_util.py     # 日志工具
│   ├── mydb.py         # 数据库操作工具
│   ├── readFile.py     # 文件读取工具
│   └── writeFile.py    # 文件写入工具
├── data/               # 测试数据
│   ├── common.yml      # 通用配置
│   ├── tmp.yml         # 临时数据（如 token）
│   └── userInfo.yml    # 用户信息测试数据
├── reports/            # 测试报告
├── temp/               # 临时数据
├── logs/               # 日志文件
├── conftest.py         # pytest 配置文件
├── runMain.py          # 主运行文件
└── pytest.ini          # pytest 配置文件
```

## 技术栈

- **Python 3.12**
- **Requests** - HTTP 请求库
- **Pytest** - 测试框架
- **Allure** - 测试报告生成工具
- **YAML** - 测试数据管理
- **MySQL** - 数据库操作

## 环境搭建

### 1. 安装 Python

确保安装了 Python 3.12 或更高版本。

### 2. 安装依赖包

```bash
pip install requests pytest allure-pytest pyyaml pymysql
```

### 3. 安装 Allure 命令行工具

- 下载 Allure 命令行工具：https://github.com/allure-framework/allure2/releases
- 解压并将 bin 目录添加到系统环境变量中

### 4. 配置测试环境

- 修改 `data/common.yml` 文件中的基础配置：
  ```yaml
  headers:
    Content-Type: application/json
  pre_url: http://your-api-host:port  # 修改为你的 API 主机地址
  ```

- 修改 `data/userInfo.yml` 文件中的测试数据：
  ```yaml
  register:
    - ["username1", "password1", "13800138001", 0, "注册成功"]
    - ["username2", "password2", "13800138002", 0, "注册成功"]
  login:
    - ["13800138001", "password1", 0, "登录成功"]
    - ["13800138002", "password2", 0, "登录成功"]
  ```

- 修改 `conftest.py` 文件中的数据库配置：
  ```python
  # 在 utils/mydb.py 中配置数据库连接信息
  ```

## 运行测试

### 方法一：直接运行 runMain.py

```bash
python runMain.py
```

该脚本会执行以下操作：
1. 运行所有测试用例并生成 Allure 原始数据
2. 生成 Allure 测试报告
3. 自动打开测试报告

### 方法二：使用 pytest 命令运行

```bash
# 运行所有测试并生成报告
pytest --alluredir=./temp
allure generate ./temp -o reports
allure open reports

# 运行指定测试文件
pytest test_cases/test_01_register.py --alluredir=./temp
```

## 测试功能

### 1. 注册测试
- 测试用户注册功能
- 验证注册成功后的响应信息

### 2. 登录测试
- 测试用户登录功能
- 验证登录成功后的响应信息
- 保存登录后的 token 和 userId 到临时文件

### 3. 获取用户信息测试
- 测试获取用户信息功能
- 使用登录时保存的 token 和 userId
- 验证获取用户信息成功后的响应信息

### 4. 创建订单测试
- 测试创建订单功能
- 使用登录时保存的 token 和 userId
- 验证创建订单成功后的响应信息

## 测试报告

测试完成后，会在 `reports` 目录生成 Allure 测试报告，报告包含：
- 测试执行结果概览
- 详细的测试步骤
- 测试执行时间统计
- 请求和响应的详细信息

## 日志管理

测试过程中的日志会记录在 `logs` 目录中，按日期命名，方便问题排查。

## 数据库操作

项目使用 `mydb.py` 工具类操作数据库，主要用于测试环境的预置和清理：
- 测试前的环境准备
- 测试后的环境恢复（如删除测试数据）

## 注意事项

1. 确保 API 服务可以正常访问
2. 确保数据库连接配置正确
3. 测试前请确保测试数据的准确性
4. 如需修改测试流程，请修改相应的 API 类和测试用例

## 扩展建议

1. 添加更多测试场景，如：
   - 产品管理测试
   - 订单管理测试
   - 支付流程测试
   - 异常场景测试

2. 优化测试框架：
   - 添加数据驱动测试
   - 实现测试用例的参数化
   - 增加测试环境的配置管理
   - 实现测试结果的邮件通知
   - 添加接口性能测试

## 许可证

本项目仅供学习和参考使用。

## 作者

- 项目创建时间：2026年
- 测试框架：Python + Requests + Pytest + Allure
