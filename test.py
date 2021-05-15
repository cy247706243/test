# -*- coding:utf-8 -*-
"""
说明：题目一的代码
"""
import json
from PIL import Image

#test 1
with open('./boxes.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    data = json_data["boxes"][0]['rectangle']
    print(data)

#test 2
img_1 = Image.open("/home/ccy/Desktop/6.png")
img_2 = Image.open("/home/ccy/Desktop/7.png")


img_3 = img_1.resize((200,290))
x1 = data['left_top'][0]
y1 = data['left_top'][1]
x2 = data['right_bottom'][0]
y2 = data['right_bottom'][1]
box = (x1,y1,x2,y2)
img_2.paste(img_3, box)
img_2.show()
#img.save("777.jpg")   # 存储图片

