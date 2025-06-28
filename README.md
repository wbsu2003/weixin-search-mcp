# 微信文章搜索MCP服务

这是一个基于FastAPI的微信文章搜索MCP服务，提供了通过关键词搜索微信公众号文章的功能。

## 使用Docker运行

### 构建镜像

在项目根目录下执行以下命令构建Docker镜像：

```bash
docker build -t weixin-search-mcp .
```

### 运行容器

构建完成后，执行以下命令运行容器：

```bash
docker run -d -p 8000:8000 --name weixin-search weixin-search-mcp
```

### 访问服务

服务启动后，可以通过浏览器访问以下地址：

- Web界面: http://localhost:8000
- API文档: http://localhost:8000/docs

## API端点

- `GET /health` - 健康检查接口
- `POST /search_articles` - 微信文章搜索接口

## 本地开发

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行服务

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
``` 

更多说明
- 博客： [微信公众号文章搜索MCP服务weixin_search_mcp](https://laosu.tech/2025/06/27/微信公众号文章搜索MCP服务weixin_search_mcp)
- 公众号： [微信公众号文章搜索MCP服务weixin_search_mcp](https://mp.weixin.qq.com/s/mYn2xaoIVom9zptCMIxvLA?token=1229315886&lang=zh_CN)
- CSDN： [微信公众号文章搜索MCP服务weixin_search_mcp](https://blog.csdn.net/wbsu2004/article/details/148946597)



