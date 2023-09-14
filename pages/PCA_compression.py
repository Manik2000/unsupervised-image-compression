"""
Subpage with image compression through PCA. 
"""
import streamlit as st
from io import BytesIO

from scripts.pca_compression import PCACompressor
from scripts.utils import *


st.set_page_config(page_title="PCA", page_icon=":fire:")

st.markdown("# PCA compression")
st.sidebar.header("Instructions")
st.sidebar.markdown(
    """
    Please upload the image, choose the number of principal compopnents to use for compression.

    Then click the button and see the results!
    """
)

uploaded_image = st.file_uploader("Upload your image")

number = st.number_input("Number of principal components", min_value=1, max_value=500, value=100, step=1)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True
    
st.button("Compress", on_click=click_button)

if st.session_state.clicked:
    if uploaded_image is not None:
        image_array = load_image_into_array(uploaded_image)
        if image_array is None:
            st.write("That is an invalied image file. Please try again.")
        else:
            compressor = PCACompressor(image_array)
            compressed_array = compressor.compress(number)
            compressed_image = load_array_into_image(compressed_array)

            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded_image, caption="Original image")
            with col2:
                st.image(compressed_image, caption="Compressed image")

            initial_file_name = uploaded_image.name.split(".")[0]
            buffer = BytesIO()
            compressed_image.save(buffer, format="JPEG")
            byte_image = buffer.getvalue()

            st.download_button("Download compressed image", 
                                data=byte_image, 
                                file_name=f"{initial_file_name}_pca_compressed.jpg")
    else:
        st.write("Please upload an image first.")
