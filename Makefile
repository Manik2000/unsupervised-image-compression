streamlit:
	streamlit run Main_page.py

build:
	docker build -t streamlit:latest .

run:
	docker run -p 8501:8501 streamlit:latest

docker-all: build run