FROM python:3.12.2-alpine3.19

WORKDIR /app_python
RUN adduser -D user && chown -R user /app_python
RUN mkdir /app_python/vol && chown -R user:user /app_python/vol

COPY --chown=user:user requirements.txt ./

RUN pip install -r requirements.txt

COPY --chown=user:user app.py ./
COPY --chown=user:user templates/ ./templates/

USER user
EXPOSE 8080

ENTRYPOINT ["sh", "-c", "python -m uvicorn app:app --host 0.0.0.0 --port 8080"]
