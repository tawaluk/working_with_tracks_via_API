FROM python:3.10
WORKDIR /track_app
COPY . /track_app/

RUN pip install -r requirements.txt
EXPOSE 8888
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
