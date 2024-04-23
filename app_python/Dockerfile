FROM python:3.9-alpine

WORKDIR /app

RUN adduser -D testUser && chown -R testUser /app
USER testUser

COPY requirements.txt .

RUN mkdir volume && \
    touch volume/visits.txt
    
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]