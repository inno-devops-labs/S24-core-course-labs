FROM python:3.9.18-alpine3.19

WORKDIR /app_python

RUN adduser -D new_user && chown -R new_user /app_python
USER new_user

COPY requirements.txt app.py ./

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt 

CMD [ "python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]