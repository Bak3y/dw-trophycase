FROM python:3.8-alpine 
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt 
COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["app.py"]
