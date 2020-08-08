FROM python:3.8.5
MAINTAINER subin.plakkannickal@gmail.com

COPY . /python_expt
WORKDIR /python_expt

RUN pip install --no-cache-dir -r requirements.txt
RUN pytest -v --junitxml="reports/result.xml"
