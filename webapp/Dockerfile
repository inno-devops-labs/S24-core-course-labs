FROM python:3-alpine3.15

RUN adduser -D myuser

RUN mkdir -p /app

COPY --chown=myuser:myuser requirements.txt /app/

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=myuser:myuser . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

USER myuser

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]