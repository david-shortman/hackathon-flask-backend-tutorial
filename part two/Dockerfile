FROM python:alpine3.7 
COPY requirements.txt run.py server.py /app/
WORKDIR /app
RUN pip install -r requirements.txt 
ARG OPEN_WEATHER_API_KEY
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:$PORT server:app