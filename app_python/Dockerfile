FROM python:3.12-slim

WORKDIR /var/www

COPY . .

RUN groupadd -g 10001 user &&\
    useradd -m -u 10000 -g user user &&\
    chown -R user:user /var/www &&\
    apt-get update && apt-get install -y make

USER user

ENV PATH $PATH:/home/user/.local/bin

RUN pip install --user pipenv && make build 

CMD ["make", "run"]
