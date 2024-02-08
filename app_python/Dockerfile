FROM python:3.10.13-alpine3.19

WORKDIR /app
EXPOSE 5000
RUN ["adduser", "-Ds", "/usr/bin/nologin", "flask"]
COPY requirements.txt *.py /app/
# Note: keeping the project files owned by root so
# the web server has less privileges over them
USER flask:flask
RUN ["pip", "install", "--user", "-r", "requirements.txt"]
CMD ["python", "main.py"]
