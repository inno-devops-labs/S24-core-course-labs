# Use the official Dart image from Docker Hub.
FROM dart:stable AS build

# Set the working directory in the Docker image filesystem.
WORKDIR /app

# Copy the Dart package manifest.
COPY pubspec.* ./
# Install dependencies (including `pub get`).
RUN dart pub get

# Copy the rest of the source code.
COPY . .

# Build the application.
RUN dart pub get --offline

# Compile the Dart application.
RUN dart compile exe bin/server.dart -o bin/server

# Build minimal serving image from AOT-compiled `bin/server`
# and the pre-built AOT-runtime in the `/runtime/` directory of the base image.
FROM scratch
COPY --from=build /runtime/ /
COPY --from=build /app/bin/server /app/bin/

# Start server.
EXPOSE 8080
CMD ["/app/bin/server"]