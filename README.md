# Images compression using unsupervised ML

This project is focused on applying PCA and clustering methods (mini batch K-means) to image compression problem.

`scikit-learn` implementations of both algorithms are used. More on how these methods can be used to compress images can be found in the [notebooks](notebooks/) directory. 

**Note:** Python >= 3.10 is required!

### Web application

Web application is deployed on Streamlit Community Cloud.
You can experiment and have fun on your own [here :fire:](https://unsupervised-ml-image-compression.streamlit.app/).

### Results

Below you can see an examplary output of using clustering for image compression.

|Original image | Compressed image with K = 10 | Compressed image with K = 50 |
|---| --- | ---|
|![](images/drops.jpg)| ![](images/k_10.png)| ![](images/k_50.png)|
||||


### Project structure

```
.
├── Dockerfile <- Dockerfile for building the image
├── Main_page.py <- main Python file defining Streamlit app
├── README.md
├── images <- directory with sample images
├── notebooks 
│   ├── clustering.ipynb <- notebook showcasing clustering compression
│   └── pca.ipynb <- notebook showcasing PCA compression
├── pages
│   ├── Clustering_compression.py <- sybpage with clustering compression
│   └── PCA_compression.py <- subpage with PCA compression
├── requirements.txt <- required packages
└── scripts
    ├── __init__.py <- makes scripts a module
    ├── cluster_compression.py <- ClusterCompressor class
    ├── pca_compression.py <- PCACompressor class
    └── utils.py <- uitilty functions for image to array and array to image conversion
```

### Running the application

Clone this repository and navigate to the root directory of the project.

* Python virtual environment

    1. Create a virtual environment (below named env) and activate it
    ```bash
    python3 -m venv env
    source env/Scripts/activate # bash
    env\Scripts\activate # on Windows
    ```
    2. Install required packages
    ```bash
    pip install -r requirements.txt
    ```
    3. Run the application
    ```bash
    streamlit run Main_page.py
    ```

* Docker

    1. Build docker image (named `my_app_image`)
    ```bash
    docker build -t my_app_image .
    ```
    2. Run the container
    ```bash
    docker run -p 8501:8501 my_app_image
    ```
