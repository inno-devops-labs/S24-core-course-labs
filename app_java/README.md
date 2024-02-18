# Anonymous threats sender
API to send threats to intimidate your enemies

![CI badge](https://github.com/FK12344321/S24-core-course-labs/actions/workflows/app_java.yaml/badge.svg)

## Description
A java app that connects to the smpt server and sends messages from an anonymous email  

## Getting Started

### Dependencies
* Docker 20.10.12

## Configuration 
Before running the app create a file `src/main/resources/mailing.properties` and add the following properties to it
```
mailing.email=<eamil of an anonymous email>
mailing.password=<password for that email>
mailing.host=<smtp server address> 
```

## How to run after configuring the app
* build a docker image 
```bash
docker build -t ats . 
```
* run the docker container  
```bash 
docker run -p 8081:8081 ats 
```

## API 
* POST /api/receivers
  **body:** {"alias": "threat-receiver-alias", "email": "threat-receiver-email"}
  **description:** creates a receiver
* POST /api/messages
  **body:** {"alias": "threat-receiver-alias", "content": "your content"}
  **description:** sends an anonimized threat to an existing receiver 

## Docker
Here how you can:
* build and push the image
  ```bash
  docker build -t anon_threats .
  docker image tag anon_threats fk12344321/anon_threats:v1.0.0
  docker push fk12344321/anon_threats:v1.0.0
  ```
* pull the image
  ```bash 
  docker pull fk12344321/anon_threats:v1.0.0
  ```
* run the image
  ```bash
  docker run fk12344321/anon_threats:v1.0.0
  ```

## CI

Github actions is used for setting up a CI pipeline that have the following jobs:
* code quality check
* security check
* docker image build and push