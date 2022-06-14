FROM python:3
WORKDIR /app
EXPOSE 5000
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "./run.py"]

