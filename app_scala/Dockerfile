FROM sbtscala/scala-sbt:eclipse-temurin-jammy-21.0.2_13_1.9.8_2.13.12 as build

RUN adduser --disabled-login user
WORKDIR /home/user

COPY build.sbt build.sc ./
COPY public/ public/
COPY project/ project/
COPY conf/ conf/
COPY app/ app/

RUN mkdir target && \
    chmod a+w target/ && \
    mkdir project/target && \
    chmod a+w project/target
USER user
RUN sbt clean compile stage

FROM openjdk:22-slim-bullseye

RUN adduser --disabled-login user
WORKDIR /home/user

COPY --from=build /home/user/target/universal/stage /app

EXPOSE 9000

RUN mkdir /app/run && chmod o+w /app/run

USER user
CMD /app/bin/app_scala -Dplay.http.secret.key=$SECRET_KEY -Dpidfile.path=/app/run/pidfile

# QCY?tAnfk?aZ?iwrNwnxIlR6CTf:G3gf:90Latabg@5241AB`R5W:1uDFN];Ik@n