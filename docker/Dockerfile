
FROM python:3.12-alpine
#FROM python:3.10

WORKDIR /app/src
ADD docker/requirements.txt /app/docker/requirements.txt

RUN pip install --upgrade pip
RUN pip install --upgrade -r /app/docker/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN rm -rf /app/docker/requirements.txt
ADD . /app

ENV TZ Asia/Shanghai
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

#CMD ["python3", "main.py"]
