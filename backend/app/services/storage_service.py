import os
import uuid
from fastapi import UploadFile
import aiofiles

class StorageService:
    def __init__(self):
        # 初始化存储目录
        self.upload_dir = "backend/uploads"
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)
    
    async def save_file(self, file: UploadFile) -> str:
        # 生成唯一文件名
        file_extension = os.path.splitext(file.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(self.upload_dir, unique_filename)
        
        # 保存文件
        try:
            async with aiofiles.open(file_path, 'wb') as out_file:
                content = await file.read()
                await out_file.write(content)
            return file_path
        except Exception as e:
            raise Exception(f"文件保存失败: {str(e)}")
    
    def delete_file(self, file_path: str) -> bool:
        # 删除文件
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            return False
        except Exception as e:
            print(f"文件删除失败: {str(e)}")
            return False
    
    def get_file_url(self, file_path: str) -> str:
        # 获取文件URL（这里返回相对路径，实际部署时可能需要返回完整URL）
        return file_path
