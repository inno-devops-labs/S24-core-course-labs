FROM python:3.9.18-alpine3.19 as build

RUN adduser -D user
WORKDIR /home/user

COPY src src
COPY requirements.txt requirements.txt
COPY test_requirements.txt test_requirements.txt

USER user
ENV VIRTUAL_ENV=venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt

#FROM scratch
EXPOSE 80
CMD ["venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
