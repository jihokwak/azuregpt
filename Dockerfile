FROM continuumio/miniconda3:latest
COPY requirements.txt ./
RUN apt-get update
RUN apt install -y uwsgi
RUN pip install -r requirements.txt
RUN mkdir -p /app
WORKDIR /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
