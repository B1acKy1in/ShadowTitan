FROM python:3.8-alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk update && apk add --no-cache bash build-base coreutils \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && python -m pip install --upgrade pip \
    && pip install -U setuptools pip \
    && pip install fastapi uvicorn[standard] requests
