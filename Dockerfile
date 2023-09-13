# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./pages ./scripts ./Main_page.py ./requirements.txt ./app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r ./app/requirements.txt

# Run streamlit app
ENTRYPOINT ["streamlit", "run", "Main_page.py", "--server.port=8501", "--server.address=0.0.0.0"]
