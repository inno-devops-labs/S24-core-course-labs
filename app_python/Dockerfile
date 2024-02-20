FROM python:3.11-slim-bullseye

WORKDIR /project

# Use non-root user
RUN useradd -m appuser && \
    chown -R appuser /project
USER appuser

# Install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app ./app

EXPOSE 8000

CMD [ "python", "-m", "flask", "--app", "app/main:app", "run", "--host=0.0.0.0", "--port=8000"]
