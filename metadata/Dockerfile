FROM python:3.9.10-buster
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        python3 \
        python3-pip \
WORKDIR /usr/share/git/eve
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .