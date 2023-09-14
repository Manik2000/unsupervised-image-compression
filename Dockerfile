FROM python:3.11-slim-bookworm

WORKDIR /app

COPY . .

EXPOSE 8501

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "Main_page.py", "--server.port=8501", "--server.address=0.0.0.0"]