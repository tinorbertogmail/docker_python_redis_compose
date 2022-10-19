FROM python:3
COPY . /app
WORKDIR /app
RUN pip install redis
CMD python python_redis.py