# Images compression using unsupervised ML

This project is focused on applying PCA and clustering methods (mini batch K-means) to image compression problem.

**Note** that Python >= 3.10 is required.


### Web application

Web application is deployed on Streamlit Community Cloud and can be found [here](https://unsupervised-ml-image-compression.streamlit.app/).

## Project structure

```
.
├── LICENSE
├── README.md
├── .gitignore
├── images
├── notebooks/
│   ├── pca.ipynb
│   └── clustering.ipynb
├── pages/
│   ├── PCA_compression.py
│   └── Clustering_compression.py
├── scripts/
│   ├── __init__.py
│   ├── pca_compressor.py
│   ├── cluster_compressor.py
│   └── utils.py
├── requirements.txt
├── Dockerfile
├── Makefile
└── Main_Page.py
```

## Running the application

