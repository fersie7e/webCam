import streamlit as st
from PIL import Image

with st.expander("start_camera"):
    camera_image = st.camera_input("camera")


if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow to grayScale
    gray_img = img.convert("L")

    # Render de image on the web page
    st.image(gray_img)