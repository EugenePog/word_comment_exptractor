FROM python:latest
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

MAINTAINER Evgeniy Pog

RUN mkdir -p /home/app
RUN mkdir -p /root/.streamlit

COPY ./app /home/app
COPY requirements.txt ./

RUN apt-get update
RUN apt-get install -y python3
RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

EXPOSE 8501

#CMD ["python", "/home/app/front_page.py"]
CMD ["streamlit", "run", "/home/app/front_page.py"]
