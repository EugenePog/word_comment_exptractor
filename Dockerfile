FROM python:latest

MAINTAINER Evgeniy

RUN mkdir -p /home/app

COPY ./app /home/app
COPY requirements.txt ./

RUN sudo apt install python3.5.0 
RUN C:\Python\python.exe -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/home/app/front_page.py"]
