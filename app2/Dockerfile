#Base image
FROM python:3.9-slim
#set working directory
WORKDIR /app2
#Copy requirements file
COPY requirements.txt .
#Install dependencies
RUN pip install -r requirements.txt
#Copy application code
COPY app.py .
#Expose port
EXPOSE 5001
#Run the application
CMD ["python", "app.py"]