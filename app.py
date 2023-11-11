import os
import streamlit as st
# from transformers import pipeline
from PIL import Image

# pipeline = pipeline(task="image-classification", model="julien-c/hotdog-not-hotdog")



st.title("Helmet Detection App: ⛑")
confidence=st.slider("Confidence score (0-0.9)", 
            min_value=0.0, 
            max_value=.9,
            value=.5,
            step=.1)
file_name = st.file_uploader("Upload an image where workers may or may not wear helmets.")

if file_name is not None:
    col1, col2 = st.columns(2)

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