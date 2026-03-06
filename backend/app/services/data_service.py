import mysql.connector
from mysql.connector import Error
import os
from app.models.schemas import UserCreate

class DataService:
    def __init__(self):
        # 初始化数据库连接
        self.connection = None
        self.cursor = None
        self.connect()
    
    def connect(self):
        # 连接到MySQL数据库
        try:
            # 这里使用默认的连接参数，实际部署时应该从环境变量或配置文件中获取
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="freshid"
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("数据库连接成功")
            # 创建表（如果不存在）
            self.create_tables()
        except Error as e:
            print(f"数据库连接失败: {e}")
            # 当数据库连接失败时，使用内存存储作为替代
            self.connection = None
            self.memory_storage = {
                "users": [],
                "predictions": []
            }
    
    def create_tables(self):
        # 创建用户表
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        # 创建预测记录表
        create_predictions_table = """
        CREATE TABLE IF NOT EXISTS predictions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            prediction JSON NOT NULL,
            file_path VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        try:
            self.cursor.execute(create_users_table)
            self.cursor.execute(create_predictions_table)
            self.connection.commit()
            print("表创建成功")
        except Error as e:
            print(f"表创建失败: {e}")
    
    async def create_user(self, user: UserCreate) -> int:
        # 创建用户
        if self.connection is not None:
            try:
                query = "INSERT INTO users (username, email) VALUES (%s, %s)"
                values = (user.username, user.email)
                self.cursor.execute(query, values)
                self.connection.commit()
                return self.cursor.lastrowid
            except Error as e:
                print(f"创建用户失败: {e}")
                # 使用内存存储作为替代
                return self._create_user_in_memory(user)
        else:
            # 使用内存存储
            return self._create_user_in_memory(user)
    
    async def get_user(self, user_id: int) -> dict:
        # 获取用户信息
        if self.connection is not None:
            try:
                query = "SELECT * FROM users WHERE id = %s"
                self.cursor.execute(query, (user_id,))
                user = self.cursor.fetchone()
                return user
            except Error as e:
                print(f"获取用户失败: {e}")
                # 使用内存存储作为替代
                return self._get_user_in_memory(user_id)
        else:
            # 使用内存存储
            return self._get_user_in_memory(user_id)
    
    async def save_prediction(self, prediction: dict, file_path: str) -> int:
        # 保存预测记录
        if self.connection is not None:
            try:
                import json
                query = "INSERT INTO predictions (prediction, file_path) VALUES (%s, %s)"
                values = (json.dumps(prediction), file_path)
                self.cursor.execute(query, values)
                self.connection.commit()
                return self.cursor.lastrowid
            except Error as e:
                print(f"保存预测记录失败: {e}")
                # 使用内存存储作为替代
                return self._save_prediction_in_memory(prediction, file_path)
        else:
            # 使用内存存储
            return self._save_prediction_in_memory(prediction, file_path)
    
    async def get_predictions(self) -> list:
        # 获取预测记录列表
        if self.connection is not None:
            try:
                query = "SELECT * FROM predictions ORDER BY created_at DESC"
                self.cursor.execute(query)
                predictions = self.cursor.fetchall()
                return predictions
            except Error as e:
                print(f"获取预测记录失败: {e}")
                # 使用内存存储作为替代
                return self.memory_storage["predictions"]
        else:
            # 使用内存存储
            return self.memory_storage["predictions"]
    
    def _create_user_in_memory(self, user: UserCreate) -> int:
        # 在内存中创建用户
        user_id = len(self.memory_storage["users"]) + 1
        user_data = {
            "id": user_id,
            "username": user.username,
            "email": user.email,
            "created_at": "2026-03-05T12:00:00"
        }
        self.memory_storage["users"].append(user_data)
        return user_id
    
    def _get_user_in_memory(self, user_id: int) -> dict:
        # 在内存中获取用户
        for user in self.memory_storage["users"]:
            if user["id"] == user_id:
                return user
        return None
    
    def _save_prediction_in_memory(self, prediction: dict, file_path: str) -> int:
        # 在内存中保存预测记录
        prediction_id = len(self.memory_storage["predictions"]) + 1
        prediction_data = {
            "id": prediction_id,
            "prediction": prediction,
            "file_path": file_path,
            "created_at": "2026-03-05T12:00:00"
        }
        self.memory_storage["predictions"].append(prediction_data)
        return prediction_id
    
    def __del__(self):
        # 关闭数据库连接
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
