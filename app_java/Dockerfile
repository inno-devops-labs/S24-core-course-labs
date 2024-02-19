FROM ubuntu:22.04 AS source
WORKDIR /archive
RUN apt update && apt install wget unzip -y
RUN wget https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-zip-file.zip && unzip sample-zip-file.zip && rm sample-zip-file.zip

FROM ubuntu:22.04
COPY --from=source /archive/sample.txt /archive/sample.txt