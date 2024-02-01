FROM python:3.9.18-alpine3.19

WORKDIR /app_python

RUN adduser -D newuser && chown -R newuser /app_python
USER newuser

COPY main.py requirements.txt ./
RUN pip install --no-cache-dir --user -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]