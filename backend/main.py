from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from app.api.routes import api_router
from app.services.model_service import ModelService

# 初始化FastAPI应用
app = FastAPI(
    title="FreshID API",
    description="FastAPI后端系统，集成已训练模型",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化模型服务
model_service = ModelService()

# 注册API路由
app.include_router(api_router, prefix="/api")

# 健康检查端点
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "服务运行正常"}

# 根路径
@app.get("/")
def read_root():
    return {"message": "Welcome to FreshID API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
