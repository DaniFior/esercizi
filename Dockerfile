FROM python:3.10-alpine 
ADD myapp.py .
ADD pippo.py .
ADD topolino.py .
CMD ["python","./myapp.py", "./topolino.py", "./pippo.py"]