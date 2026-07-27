# water-backend

水利水资源管理后端系统，基于 FastAPI 构建，提供水库信息管理、调度数据管理、多目标优化（NSGA-II）以及知识图谱问答等功能。

## 功能模块

| 模块 | 说明 |
|---|---|
| **水库数据管理** | 水库、水闸、泵站等水利设施信息的增删改查 |
| **调度数据管理** | 水资源调度记录的存储与查询 |
| **多目标优化** | 基于 NSGA-II 遗传算法的水资源多目标优化调度 |
| **知识图谱问答** | 基于 Neo4j 图数据库的水利领域知识图谱构建与自然语言问答 |

## 技术栈

- **语言**: Python 3
- **Web 框架**: [FastAPI](https://fastapi.tiangolo.com/)
- **关系型数据库**: MySQL（SQLAlchemy ORM）
- **图数据库**: Neo4j
- **数据校验**: Pydantic
- **优化算法**: NSGA-II（非支配排序遗传算法 II）

## 项目结构

```
water-backend/
├── app/
│   ├── api/v1/              # API 路由（v1）
│   │   ├── reservoir.py     # 水库相关接口
│   │   ├── regulation.py    # 调度相关接口
│   │   ├── optimize.py      # 优化算法接口
│   │   └── kg_qa.py         # 知识图谱问答接口
│   ├── models/
│   │   ├── mysql/           # MySQL ORM 模型
│   │   └── neo4j/           # Neo4j 图模型（节点 & 关系）
│   ├── services/            # 业务逻辑层
│   │   ├── nsga2_service.py # NSGA-II 优化服务
│   │   ├── kg_service.py    # 知识图谱查询服务
│   │   └── qa_service.py    # 问答服务
│   ├── schemas/             # Pydantic 数据校验
│   ├── core/                # 核心配置（数据库连接、安全等）
│   ├── utils/               # 工具函数（日志、数据清洗、响应封装）
│   └── main.py              # 应用入口
├── docs/                    # 文档（数据库设计、接口文档、会议记录）
├── tests/                   # 测试
├── data/                    # 数据文件（原始数据 & 导入脚本）
├── requirements.txt         # Python 依赖
└── .env.example             # 环境变量模板
```

## 快速开始

### 环境要求

- Python 3.10+
- MySQL 8.0+
- Neo4j 5.x

### 安装

```bash
# 克隆项目
git clone <repo-url>
cd water-backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux / macOS
# venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt
```

### 配置

复制环境变量模板并填写实际配置：

```bash
cp .env.example .env
```

编辑 `.env` 文件，配置 MySQL 和 Neo4j 连接信息。

### 启动

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

启动后访问：
- API 文档 (Swagger UI): http://localhost:8000/docs
- API 文档 (ReDoc): http://localhost:8000/redoc

## API 概览

| 方法 | 路径 | 说明 |
|---|---|---|
| GET/POST/PUT/DELETE | `/api/v1/reservoir` | 水库信息管理 |
| GET/POST/PUT/DELETE | `/api/v1/regulation` | 调度记录管理 |
| POST | `/api/v1/optimize` | 执行多目标优化 |
| POST | `/api/v1/kg_qa` | 知识图谱问答 |
