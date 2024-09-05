FROM python:3.10-alpine
ADD server.py .
ADD requirements.txt .
RUN mkdir ./templates
COPY ./templates/index.html ./templates
RUN pip3 install -r requirements.txt
CMD ["python", "./server.py"]

#per fare build: docker build -t flask-container .
#per fare run: docker run -d -p 8085:8085 flask-container 