FROM python:3.12.2-alpine3.19 as builder

WORKDIR /app

COPY main.py requirements.txt ./

RUN pip install --no-cache-dir --requirement requirements.txt \
    && pip install --no-cache-dir pyinstaller==6.4.0 \
    && apk add --no-cache binutils=2.41-r0 \
    && pyinstaller --onefile main.py

FROM alpine:3.19

WORKDIR /app

COPY --from=builder /app/dist/main /app/main
COPY templates ./templates

EXPOSE 8000

RUN adduser -D myuser \
    && mkdir -p visits \
    && chown -R myuser:myuser /app
    
USER myuser

CMD ["./main"]
