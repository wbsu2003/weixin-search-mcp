from fastapi import FastAPI, HTTPException
from fastapi_mcp import FastApiMCP
from miku_ai import get_wexin_article
from pydantic import BaseModel
from typing import List
import uvicorn
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

# 创建FastAPI应用
app = FastAPI(
    title="微信文章搜索MCP服务",
    description="基于miku_ai库的微信文章搜索MCP服务，支持SSE协议",
    version="1.0.0"
)

# 挂载静态文件目录
app.mount("/img", StaticFiles(directory="img"), name="img")

# 定义数据模型
class ArticleResponse(BaseModel):
    title: str
    url: str
    source: str
    date: str

class ArticleSearchRequest(BaseModel):
    query: str
    top_num: int = 5  # 添加可选参数，默认为5条

class ArticleSearchResponse(BaseModel):
    articles: List[ArticleResponse]
    total_count: int

# 文章搜索端点
@app.post("/search_articles", response_model=ArticleSearchResponse)
async def search_articles(request: ArticleSearchRequest):
    """搜索微信文章"""
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="查询参数不能为空")
    
    articles = await get_wexin_article(request.query.strip(), request.top_num)
    
    output_articles = [
        ArticleResponse(
            title=article.get('title', ''),
            url=article.get('url', ''),
            source=article.get('source', ''),
            date=article.get('date', '')
        ) for article in articles
    ]
    
    return ArticleSearchResponse(
        articles=output_articles,
        total_count=len(output_articles)
    )

# 健康检查端点
@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "微信文章搜索MCP"}

# 根路由返回 HTML 页面
@app.get("/", include_in_schema=False)
async def root():
    """返回首页 HTML"""
    return FileResponse("index.html")

# 初始化MCP服务（无base_url参数）
mcp = FastApiMCP(
    app,
    name="微信文章搜索服务",
    description="通过SSE协议提供微信文章搜索功能"
)

# 挂载MCP路由
mcp.mount()

# 必须在所有路由定义后调用
mcp.setup_server()

if __name__ == "__main__":
    # 使用导入字符串格式解决reload问题
    uvicorn.run(
        "main:app",  # 关键修正：使用字符串格式
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
