# Use official Python image as base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy app code and requirements file
COPY app.py ./
COPY requirements.txt ./

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 9001 (default Streamlit port)
EXPOSE 9001

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=9001", "--server.address=0.0.0.0"]    