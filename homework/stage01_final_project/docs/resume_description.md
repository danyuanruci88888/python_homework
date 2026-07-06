# 简历项目描述

## AI 就业陪跑任务管理系统后端

### 项目描述

基于 FastAPI 构建面向应届生求职准备场景的后端系统，支持学生注册登录、学习任务管理、岗位收藏、投递记录、技能标签管理和学习进度统计。项目使用 MySQL 持久化业务数据，Redis 缓存统计结果，JWT 实现接口鉴权，并通过 Docker Compose 编排本地部署环境。

### 技术栈

- Python 3.11
- FastAPI
- SQLAlchemy
- MySQL 8
- Redis 7
- Docker / Docker Compose
- JWT
- Pydantic

### 项目亮点

1. **分层架构设计**：采用 router、service、schema、model 分层结构，提升项目可维护性。
2. **JWT 用户认证**：使用 JWT 实现登录鉴权，并通过 `user_id` 实现用户数据隔离。
3. **Redis 缓存加速**：学习进度统计接口使用 Redis 缓存，减少重复数据库查询。
4. **完整求职跟踪链路**：实现岗位收藏、投递记录、投递状态变更，覆盖求职准备核心场景。
5. **技能标签管理**：支持用户维护个人技能标签，为后续 AI 岗位匹配和学习计划生成打下基础。
6. **工程化能力**：提供 Swagger 接口文档、README 启动说明和 Docker Compose 一键部署，便于测试和演示。
