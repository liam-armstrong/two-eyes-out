 FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
 COPY start.sh /start.sh
 EXPOSE 8000
 RUN chmod +x start.sh
 ENTRYPOINT ["sh", "/start.sh"]