FROM python

COPY . /app_python
WORKDIR /app_python

RUN adduser local && chown -R local /app_python
USER local

HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:3000/ || exit 1

EXPOSE 3000

ENV FLASK_APP=app.py

RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
