#2022.4.7修改，增加了格式转换

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from ssd import SSD


crop   =   False

st.header("SSD物体识别和CNN叶片病害识别系统")
st.write("选择你需要识别的叶片图片:")

#只能输入jpg文件
uploaded_file = st.file_uploader("Choose an image...",type=["jpg", "png", "bmp", "jpeg","webp","psd","dxf","gif","apng","tif","pcx","tga","exif","fpx","svg","cdr","pcd","ufo","eps","ai","raw","WMF","avif"])

#uploaded_file = st.file_uploader("Choose an image...")


if uploaded_file is not None:

    ssd = SSD()
    #image = Image.open(uploaded_file)

    ####转成.JPG文件###
    #将输入的文件使用PIL打开给img，img以“image.jpg”保存，为了转变为.jpg格式
    img = Image.open(uploaded_file).convert('RGB')
    img.save('image.jpg',quality=95)
    #PIL打开转换后保存的.jpg图片，赋值给image，完成格式的转换
    image = Image.open('image.jpg')



    st.image(image, caption='Input Image', use_column_width=True)


    st.header('输出叶片检测结果：')
    r_image = ssd.detect_image(image)
    st.image(r_image, caption='Output Image', use_column_width=True)



    st.header('对识别叶片分别进行病害检测：')

    ssd.detect_image2(image)

