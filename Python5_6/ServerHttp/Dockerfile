FROM python:3.10-alpine
ADD server.py .
ADD requirements.txt .
RUN mkdir ./templates
COPY ./templates/index.html ./templates
RUN pip3 install -r requirements.txt
CMD ["python", "./server.py"]