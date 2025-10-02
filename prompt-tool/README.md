# README.md

# Prompt Tool

## 简介

Prompt Tool 是一个基于 Python 的快速调用提示词工具，旨在通过快捷键快速弹出不同的提示词模板，并根据用户选择的模板动态生成提示词。该工具支持在 Ubuntu 上扩展快捷键，以便用户能够高效地调用服务。

## 特性

- 根据输入的快捷键弹出不同的提示词模板。
- 支持动态生成提示词，基于用户选择的模板。
- 提供快捷键管理功能，方便用户在 Ubuntu 上进行设置。
- 代码结构清晰，易于扩展和维护。

## 目录结构

```
prompt-tool
├── src
│   ├── main.py                # 应用程序入口点
│   ├── templates
│   │   └── poetry_template.py  # 诗词模板定义
│   ├── services
│   │   └── prompt_service.py    # 提示词生成和调用服务逻辑
│   ├── utils
│   │   └── shortcut_manager.py   # 快捷键管理
│   └── types
│       └── index.py             # 类型和接口定义
├── requirements.txt             # 项目依赖
├── README.md                    # 项目文档
└── setup.py                     # 项目打包配置
```

## 安装

1. 克隆项目：

   ```bash
   git clone <repository-url>
   cd prompt-tool
   ```

2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

## 使用

1. 运行应用程序：

   ```bash
   python src/main.py
   ```

2. 根据提示设置快捷键，并选择相应的提示词模板。

## 贡献

欢迎任何形式的贡献！请提交问题或拉取请求。

## 许可证

本项目采用 MIT 许可证，详细信息请参见 LICENSE 文件。