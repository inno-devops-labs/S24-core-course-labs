FROM python:3-alpine3.15
ENV PYTHONUNBUFFERED 1
WORKDIR /app_python
RUN adduser -D user && chown -R user /app_python
USER user
COPY templates ./templates
COPY .dockerignore .
COPY app.py requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir --user
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]