#Stage 1 - Install dependencies and build the app in a build environment
FROM debian:latest AS build-env

RUN apt-get update
RUN apt-get install -y curl git unzip

# define variables
ARG FLUTTER_SDK=/usr/local/flutter
ARG FLUTTER_VERSION=3.16.9
ARG APP=/app/

#clone flutter
RUN git clone https://github.com/flutter/flutter.git $FLUTTER_SDK
# change dir to current flutter folder and make a checkout to the specific version
RUN cd $FLUTTER_SDK && git fetch && git checkout $FLUTTER_VERSION

# setup the flutter path as an enviromental variable
ENV PATH="$FLUTTER_SDK/bin:$FLUTTER_SDK/bin/cache/dart-sdk/bin:${PATH}"

# check if the installation was successful 
RUN flutter doctor -v

# create folder to copy source code
RUN mkdir $APP

# copy source code to folder
COPY . $APP

# set up the working directory
WORKDIR $APP

# Run build
RUN flutter clean
RUN flutter pub get
RUN flutter build web

# Stage 2 - Create the run-time image

# use nginx to deploy
FROM nginx:1.25.2-alpine

# copy the info of the builded web app to nginx
COPY --from=build-env /app/build/web /usr/share/nginx/html

# Expose and run nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]