from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.services.model_service import ModelService
from app.services.data_service import DataService
from app.services.storage_service import StorageService
from app.models.schemas import PredictionRequest, PredictionResponse, UserCreate, UserResponse
import os

# 创建API路由器
api_router = APIRouter()

# 依赖注入模型服务
async def get_model_service():
    from app.services.model_service import ModelService
    return ModelService()

# 依赖注入数据服务
async def get_data_service():
    from app.services.data_service import DataService
    return DataService()

# 依赖注入存储服务
async def get_storage_service():
    from app.services.storage_service import StorageService
    return StorageService()

# 上传图像并进行预测
@api_router.post("/upload", response_model=PredictionResponse)
async def upload_image(
    file: UploadFile = File(...),
    model_service: ModelService = Depends(get_model_service),
    storage_service: StorageService = Depends(get_storage_service),
    data_service: DataService = Depends(get_data_service)
):
    # 验证文件类型
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="请上传图像文件")
    
    # 保存文件
    file_path = await storage_service.save_file(file)
    
    # 进行预测
    prediction = await model_service.predict(file_path)
    
    # 存储预测记录
    prediction_id = await data_service.save_prediction(prediction, file_path)
    
    # 返回结果
    return PredictionResponse(
        success=True,
        data={
            "prediction_id": prediction_id,
            "prediction": prediction,
            "file_path": file_path
        },
        message="预测成功"
    )

# 获取预测结果列表
@api_router.get("/predictions")
async def get_predictions(
    data_service: DataService = Depends(get_data_service)
):
    predictions = await data_service.get_predictions()
    return {
        "success": True,
        "data": predictions,
        "message": "获取预测结果成功"
    }

# 创建用户
@api_router.post("/users", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    data_service: DataService = Depends(get_data_service)
):
    user_id = await data_service.create_user(user)
    return UserResponse(
        success=True,
        data={
            "user_id": user_id,
            "username": user.username
        },
        message="用户创建成功"
    )

# 获取用户信息
@api_router.get("/users/{user_id}")
async def get_user(
    user_id: int,
    data_service: DataService = Depends(get_data_service)
):
    user = await data_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return {
        "success": True,
        "data": user,
        "message": "获取用户信息成功"
    }

# 数据同步
@api_router.get("/sync")
async def sync_data(
    data_service: DataService = Depends(get_data_service)
):
    # 这里可以实现数据同步逻辑
    return {
        "success": True,
        "data": {"last_sync": "2026-03-05T12:00:00"},
        "message": "数据同步成功"
    }
