FROM python:3.8
ENV PYTHONUNBUFFERED=1
ENV FLASK_DEBUG=1
ENV FLASK_APP=main.py

WORKDIR /d_add

#copy all the files
COPY . /d_add

#Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

#Expose the required port
EXPOSE 8000

#Run the command
CMD gunicorn wsgi:application --bind 127.0.0.1:8000