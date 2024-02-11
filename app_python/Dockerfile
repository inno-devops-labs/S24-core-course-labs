FROM python:3.9.18-alpine3.19 as server

RUN adduser -D user
WORKDIR /home/user

COPY requirements.txt requirements.txt

USER user
ENV VIRTUAL_ENV=venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt

COPY src src

EXPOSE 80
CMD ["venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]

FROM server as test
WORKDIR /home/user
COPY test_requirements.txt ./
USER user
RUN pip install --no-cache-dir --upgrade -r test_requirements.txt
CMD ["venv/bin/pytest"]

