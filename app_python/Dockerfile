FROM python:3.8-slim as builder
WORKDIR /work_app

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /work_app/wheels -r requirements.txt

FROM python:3.8-slim

RUN useradd --create-home appuser
WORKDIR /work_app

COPY --from=builder /work_app/wheels /wheels
COPY --from=builder /work_app/requirements.txt .

RUN pip install --no-cache /wheels/* \
    && rm -rf /wheels \
    && rm -rf /root/.cache/pip/*


COPY ./app.py .
COPY ./templates ./templates
COPY ./test_app.py .

USER appuser

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]