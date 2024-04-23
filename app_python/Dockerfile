FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl build-essential && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y build-essential && \
    apt-get autoremove -y && \
    apt-get clean

COPY templates ./templates
COPY app.py .

RUN useradd anton && chown -R anton /app
RUN mkdir /app/vol
RUN chown -R anton:anton /app
USER anton

EXPOSE 5001

CMD python3 app.py
HEALTHCHECK CMD curl --fail http://localhost:5001/health || exit 1

STOPSIGNAL SIGKILL