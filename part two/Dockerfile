FROM python:alpine3.7 
COPY requirements.txt run.py server.py /app/
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 5001
ARG OPEN_WEATHER_API_KEY
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:5001" ]
CMD [ "server:app" ]
