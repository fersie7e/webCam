import streamlit as st
from PIL import Image

st.subheader('Conversor de imagenes a escala de grises')
uploaded_image = st.file_uploader("Upload Image")

with st.expander("start_camera"):
    camera_image = st.camera_input("camera")

print(camera_image)
print(uploaded_image)

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)
    # Convert the pillow to grayScale
    gray_img = img.convert("L")
    # Render de image on the web page
    st.image(gray_img)

if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_img = img.convert('L')
    # Display the grayscale image on the webpage
    st.image(gray_uploaded_img)