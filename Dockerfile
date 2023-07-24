FROM python:3.8.3

# set work directory
WORKDIR ./

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# copy project
COPY . ./

EXPOSE 1234

RUN python manage.py migrate
RUN python manage.py makemigrations ToDoList
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:1234"]