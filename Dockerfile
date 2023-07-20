FROM python:3.10

#some envs
WORKDIR /app

#copy local files
COPY . .

#install python dependencies
RUN pip install -r requirements.txt

#CMD ["python", "-m pytest Tests"]