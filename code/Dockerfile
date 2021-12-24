FROM python:3.7-slim
WORKDIR /app
ADD . /app
RUN apt-get update -y && apt-get install -y libgomp1
RUN pip install -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "app:app"]
EXPOSE 8000