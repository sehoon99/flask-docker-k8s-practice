# flask_app/Dockerfile

FROM python:3.10-slim         

WORKDIR /app                  # 컨테이너 내 작업 디렉토리 설정

COPY requirements.txt ./      
RUN pip install --no-cache-dir -r requirements.txt 

COPY . .                      
CMD ["python3", "app.py"]
