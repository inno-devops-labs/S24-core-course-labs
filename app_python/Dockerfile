FROM python:3-alpine3.15

WORKDIR /app_python

RUN adduser -D -s /bin/bash nonroot

COPY --chown=nonroot:nonroot ./requirements.txt /app_python

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=nonroot:nonroot app.py /app_python
COPY --chown=nonroot:nonroot templates/index.html /app_python/templates/index.html

USER nonroot

EXPOSE 5000

CMD ["cd", "app_python"]
CMD ["python", "app.py"]
