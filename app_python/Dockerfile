FROM python:3.10
RUN useradd -ms /bin/bash server
USER server

WORKDIR /app_python

COPY main.py requirements.txt .

RUN mkdir /app_python/persistent

RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD ["python3", "main.py"]
