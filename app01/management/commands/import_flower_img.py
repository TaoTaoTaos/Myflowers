import os
import sys

# 获取项目根目录的路径
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.append(project_path)

# 设置Django项目的设置模块
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Myflowers.settings")

import django

django.setup()

from django.core.files import File
from app01.models import FlowerMaterial

# 设置图片目录路径
image_dir = r"F:\Myflowers\app01\management\img\output"

# 遍历图片目录中的所有图片文件
for image_filename in os.listdir(image_dir):
    if image_filename.endswith(".png"):
        model_name = os.path.splitext(image_filename)[0]  # 获取型号名
        image_path = os.path.join(image_dir, image_filename)

        try:
            # 查找FlowerMaterial对象
            flower_material = FlowerMaterial.objects.get(model=model_name)

            # 打开图片文件
            with open(image_path, "rb") as image_file:
                flower_material.image.save(image_filename, File(image_file))

            print(f"更新 {model_name} 的图片成功")

        except FlowerMaterial.DoesNotExist:
            # 处理型号不存在的情况
            print(f"型号 {model_name} 不存在于数据库中")

print("图片导入并更新完成")

# python app01/management/commands/import_flower_img.py
