FROM python

COPY . /app_python
WORKDIR /app_python

RUN adduser local && chown -R local /app_python
USER local

HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ || exit 1

RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]