FROM golang:1.22.0-alpine3.19 as builder

WORKDIR /usr/src/app/

COPY go.mod *.go /usr/src/app/
# No dependencies yet
#RUN go mod download && go mod verify

RUN ["env", "CGO_ENABLED=0", "go", "build", "-o", "catfact_webapp", "."]


FROM scratch
# Enable https requests from within the container
COPY --from=0 /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

EXPOSE 5000

COPY --from=builder /usr/src/app/catfact_webapp /
USER 2004:2004
ENTRYPOINT ["/catfact_webapp"]
