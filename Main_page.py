"""
Main page of streamlit application.
Subpages are defined in `pages` directory.
"""
import os

import streamlit as st

st.set_page_config(
    page_title="Image compression",
    page_icon="👋",
)

st.write("# Image compression using unsupervised learning")

st.sidebar.success("Select a page.")

st.markdown(
    """
    This application enables to compress both RGB and grayscale images using unsupervised learning algorithms.
    These include mini-batch K-means, and PCA (principal component analysis).

    Select a subpage from sidebar, upload an image and have fun experienting! :fire:

    ## Example:
    Below you can see an result of applying clustering image compression to a picture of water drops.
    It is plain to see that the more clusters we use, the less compressed the image becomes.
"""
)

col1, col2, col3 = st.columns(3)

with col1:
    st.image(os.path.join("images", "drops.jpg"), caption="Original image")

with col2:
    st.image(os.path.join("images", "k_10.png"), caption="Compressed image with 10 color clusters")

with col3:
    st.image(os.path.join("images", "k_50.png"), caption="Compressed image with 50 color clusters")

st.markdown("""
    ## Code, explanations and more:
    You can find code and notebooks explaining the way the algorithms work on [Github](https://github.com/Manik2000/unsupervised-ml-image-compression).
"""
)
