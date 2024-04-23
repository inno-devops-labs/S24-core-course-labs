FROM python:3.11-slim-bookworm

WORKDIR /app_python

ARG UID=10001
ARG GID=10001

RUN groupadd -g "${GID}" user \
    && useradd -u "${UID}" -g "${GID}" user

COPY --chown=user:user ./requirements.txt /app_python

RUN pip install -r requirements.txt

COPY --chown=user:user app.py /app_python
COPY --chown=user:user templates/index.html /app_python/templates/index.html

RUN mkdir -p ./data/
RUN chown -R user:user ./
RUN chown -R user:user ./data

USER user

EXPOSE 5000

# CMD ["cd", "app_python"]
CMD ["sh", "-c", "python3 -m gunicorn --bind 0.0.0.0:5000 app:wsgi_app"]