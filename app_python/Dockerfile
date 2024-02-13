FROM python:3.9

RUN useradd --user-group --system --create-home --no-log-init app

USER app

ENV PATH /home/app/.local/bin:${PATH}

WORKDIR /app

COPY ./requirements.txt /app

RUN pip3 install --user --no-cache-dir --upgrade -r requirements.txt

COPY ./main.py /app

COPY ./template/index.html /app/template/index.html

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
