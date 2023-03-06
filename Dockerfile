# Dockerfile

# pull the official docker image
FROM python:3.11.1-slim

# set work directory


# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./app /app 




#WORKDIR /app
#RUN ["alembic", "revision",  "--autogenerate"]
#RUN ["alembic", "upgrade", "head"]
#RUN ["python", "utils/converter_postgres.py"]
WORKDIR /app/src
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


#RUN alembic revision --autogenerate -m "autoinicialisation"

#RUN alembic upgrade head
#RUN python utils/converter_postgres.py


