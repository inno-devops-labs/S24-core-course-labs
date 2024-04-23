FROM python:3.11-alpine3.19

ARG user="appuser"

RUN adduser -D $user && mkdir /app && chown -R $user /app

USER $user

ENV PATH="${PATH}:/home/$user/.local/bin"

WORKDIR /app

COPY app.py visits requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
