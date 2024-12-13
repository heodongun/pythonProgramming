# 베이스 이미지를 Python 3.10으로 설정
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /app

# 애플리케이션 코드 복사
COPY main.py /app/main.py

# FastAPI와 Uvicorn 설치
RUN pip install --no-cache-dir fastapi uvicorn

# FastAPI 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
