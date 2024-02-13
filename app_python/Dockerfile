FROM python:3.8.13-alpine3.16

WORKDIR /app_python

RUN adduser -D -s /bin/bash nonroot

COPY --chown=app:app requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=nonroot:nonroot main.py /app_python
COPY --chown=nonroot:nonroot /templates /app_python/templates

USER nonroot

EXPOSE 5000

CMD ["python", "main.py"]
