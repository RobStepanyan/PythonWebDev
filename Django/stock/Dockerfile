FROM python:latest
ADD . /stock
WORKDIR /stock
COPY requirements.txt /stock/
RUN pip install -r requirements.txt
COPY . /stock/
