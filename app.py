import os
import streamlit as st
import base64
# from transformers import pipeline
from PIL import Image
from st_clickable_images import clickable_images
# pipeline = pipeline(task="image-classification", model="julien-c/hotdog-not-hotdog")


st.title("Helmet Detection App: ⛑")
confidence=st.slider("Confidence score (0-0.9)", 
            min_value=0.0, 
            max_value=.9,
            value=.5,
            step=.1)
file_name = st.file_uploader("Upload an image where workers may or may not wear helmets.")

if (file_name is not None):
    col1, col2 = st.columns(2)
    # img1 =""
    # img2 =""
    # col1.image(img1, use_column_width=True)
    # col2.image(img2, use_column_width=True)

    image = Image.open(file_name)
    image.save("data/inputImg.jpg")
    col1.image(image, use_column_width=True)
    os.system(f"cd yolov5/ && python detect.py --weights ../best.pt --img 416 --conf {confidence} --source ../data/inputImg.jpg")
    im = Image.open("yolov5/runs/detect/exp/inputImg.jpg")
    im.save("data/output.jpg")
    im.close()
    output =Image.open("data/output.jpg")
    os.system("rm -rf yolov5/runs")
    col2.image(output, use_column_width=True)
    image.close()
    output.close()

elif (st.checkbox('Select an example by clicking on the checkbox.')):
    image_list=["https://media.istockphoto.com/id/1301722993/photo/group-of-contractors-celebrating-the-end-of-successful-construction-process.jpg?s=612x612&w=0&k=20&c=Xv7sO0AGHITZ6-SdTFrvXYnlWQ_Sc3wAcnGory4n1NA=","https://media.istockphoto.com/id/1472264590/photo/substation-maintenance-engineers.webp?b=1&s=170667a&w=0&k=20&c=dXhPK_sakEhOsAFb6InX4onVoaSgmUZ5A-V6eUlZf8E="]
    # st.markdown("select a image")
    clicked = clickable_images(
        image_list,
        titles=[f"Image #{str(i)}" for i in range(len(image_list))],
        div_style={"display": "flex", "justify-content": "space-between", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"},
        key=None,
    )
    st.markdown(f"Image # {clicked} selected" if clicked > -1 else "No image selected")
    if clicked>-1:
        col1, col2 = st.columns(2)
        file_exp =f"sample/image{clicked+1}.jpg"
        image = Image.open(file_exp)
        image.save("data/inputImg.jpg")
        col1.image(image, use_column_width=True)
        os.system(f"cd yolov5/ && python detect.py --weights ../best.pt --img 416 --conf {confidence} --source ../data/inputImg.jpg")
        im = Image.open("yolov5/runs/detect/exp/inputImg.jpg")
        im.save("data/output.jpg")
        im.close()
        output =Image.open("data/output.jpg")
        col2.image(output, use_column_width=True)
        image.close()
        output.close()
        os.system("rm -rf yolov5/runs")