FROM python:alpine3.7 
COPY requirements.txt run.py server.py /app/
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 8080
ARG OPEN_WEATHER_API_KEY
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8080" ]
CMD [ "server:app" ]
