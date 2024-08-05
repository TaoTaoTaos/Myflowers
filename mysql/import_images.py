import os
import mysql.connector

# 数据库连接配置
config = {
    "user": "rebuild",
    "password": "rebuild",
    "host": "127.0.0.1",
    "database": "rebuild30",
}

# 图片文件夹路径
image_folder = r"F:\Myflowers\app01\management\img\output"

# 连接数据库
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# 遍历图片文件夹
for filename in os.listdir(image_folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        # 获取产品型号（假设文件名即为产品型号）
        product_model = os.path.splitext(filename)[0]
        # 图片路径
        image_path = os.path.join(image_folder, filename)

        # 更新数据库中的产品记录
        update_query = "UPDATE t__product SET CHANPINGTU = %s WHERE XINGHAO = %s"
        cursor.execute(update_query, (image_path, product_model))
        print(f"Updated {product_model} with image {image_path}")

# 提交事务
conn.commit()

# 关闭数据库连接
cursor.close()
conn.close()
