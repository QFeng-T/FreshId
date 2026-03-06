import torch
from PIL import Image
import numpy as np
import os

class ModelService:
    def __init__(self):
        # 初始化模型
        self.model = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.load_model()
    
    def load_model(self):
        # 加载已训练好的模型
        model_path = "models/best_model.pth"
        if os.path.exists(model_path):
            try:
                self.model = torch.load(model_path, map_location=self.device)
                self.model.eval()
                print(f"模型加载成功: {model_path}")
            except Exception as e:
                print(f"模型加载失败: {e}")
                # 当模型加载失败时，使用一个简单的模拟模型
                self.model = None
        else:
            print(f"模型文件不存在: {model_path}")
            # 当模型文件不存在时，使用一个简单的模拟模型
            self.model = None
    
    async def predict(self, image_path):
        # 读取图像
        try:
            image = Image.open(image_path)
            image = image.resize((224, 224))  # 调整图像大小
            image = np.array(image) / 255.0  # 归一化
            image = torch.tensor(image, dtype=torch.float32).permute(2, 0, 1).unsqueeze(0).to(self.device)
        except Exception as e:
            return {"error": str(e)}
        
        # 进行预测
        if self.model is not None:
            try:
                with torch.no_grad():
                    output = self.model(image)
                    # 处理输出结果
                    if isinstance(output, torch.Tensor):
                        # 假设模型输出是分类结果
                        probabilities = torch.softmax(output, dim=1).cpu().numpy()[0]
                        class_id = np.argmax(probabilities)
                        confidence = float(probabilities[class_id])
                        return {
                            "class_id": int(class_id),
                            "confidence": confidence,
                            "label": f"Class {class_id}"
                        }
                    else:
                        return {"error": "模型输出格式不正确"}
            except Exception as e:
                return {"error": str(e)}
        else:
            # 使用模拟模型进行预测
            return {
                "class_id": 0,
                "confidence": 0.95,
                "label": "模拟预测结果",
                "message": "使用模拟模型，实际模型未加载"
            }
