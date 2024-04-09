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
RUN flutter packages pub global activate webdev
RUN flutter packages pub global run webdev build

# Stage 2 - Create the run-time image

EXPOSE 80

CMD flutter packages pub global run webdev serve