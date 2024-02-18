FROM python:3.9.18-alpine3.19

RUN adduser -D user
WORKDIR /home/user

COPY requirements.txt requirements.txt
COPY src src

USER user
ENV VIRTUAL_ENV=venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --no-cache-dir --upgrade pip==24.0 && pip install --no-cache-dir --upgrade -r requirements.txt


EXPOSE 80
CMD ["venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]

