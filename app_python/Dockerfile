FROM python:3.11-slim

RUN useradd -ms /bin/bash lab_user && \
    mkdir /home/lab_user/app && \
    chown -R lab_user /home/lab_user/app

WORKDIR /home/lab_user
USER lab_user

COPY requirements.txt .

ENV PATH="/home/lab_user/.local/bin:${PATH}"

RUN pip install --user -r requirements.txt

COPY ./ ./app

WORKDIR /home/lab_user/app

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(1); s.connect(('localhost', 5000))" || exit 1

CMD [ "python", "-u", "app.py"]