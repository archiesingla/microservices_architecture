FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask requests pandas
EXPOSE 7000
ENTRYPOINT ["python", "container2.py"]