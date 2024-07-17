import pandas as pd
import openpyxl
from openpyxl.drawing.image import Image
import os
from PIL import Image as PILImage

# 设置Excel文件路径和输出图片目录
excel_file_path = r"F:\Myflowers\app01\management\img\花材图片表.xlsx"
output_dir = r"F:\Myflowers\app01\management\img\output"

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取Excel文件
df = pd.read_excel(excel_file_path, engine="openpyxl")

# 打开Excel文件
wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

# 获取所有图片对象
images = sheet._images

# 遍历每一行，提取型号和图片
for idx, row in df.iterrows():
    model = row["型号"]
    image_saved = False

    # 遍历图片对象，找到与当前行对应的图片
    for image in images:
        # 图片的位置行数，openpyxl的行列都是从1开始
        image_row = image.anchor._from.row
        # 数据行对应的行数，加2是因为pandas的索引从0开始，而Excel从第2行开始
        data_row = idx + 2

        if image_row == data_row:
            image_path = os.path.join(output_dir, f"{model}.png")
            # 获取图片数据并保存
            pil_image = PILImage.open(image.ref)
            pil_image.save(image_path)
            image_saved = True
            break

    if not image_saved:
        print(f"第{data_row}行没有找到图片")

print("图片提取并重命名完成")
