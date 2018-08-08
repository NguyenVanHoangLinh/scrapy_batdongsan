FROM ubuntu:18.04
FROM python:3.6-onbuild
RUN  apt-get update &&apt-get upgrade -y&& apt-get install python-pip -y && pip3 install psycopg2 && pip3 install psycopg2-binary 
RUN pip3 install --upgrade pip
RUN pip3 install scrapy --upgrade
run pip3 install scrapy-splash
COPY . /scrapy_batdongsan
WORKDIR /scrapy_batdongsan
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
EXPOSE 5432
CMD scrapy crawl estate

