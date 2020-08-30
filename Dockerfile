FROM python:3.6-slim

COPY ./app app

WORKDIR /app

RUN pip install -r requirements.txt &&\
    apt-get update


EXPOSE 5000
    
CMD [ "python", "app.py" ]
    
