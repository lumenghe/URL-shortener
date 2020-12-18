FROM python:3.7.3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONPATH=/usr/src/app/

ENV FLASK_APP=url_shortener/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install required python libs
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# Copy code from current folder to /usr/src/app in container
COPY . /usr/src/app

EXPOSE 5000
#CMD ["flask", "run"]
