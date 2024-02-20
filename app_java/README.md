## Workflow Status

![Java CI Workflow](https://github.com/starkda/S24-core-course-labs/actions/workflows/java_ci.yml/badge.svg?event=push)

# Java Web Application

This is a Java web application built using Spring Boot to track how many times a specific route is accessed.

## Usage

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd project_folder
    ```

3. Build the application:

    ```bash
    mvn clean package
    ```

4. Run the application:

    ```bash
    java -jar target/<your_jar_file>.jar
    ```

5. Access the route:

   Open your web browser and navigate to `http://localhost:8080/route`.

## Testing

To run the tests:

```bash
mvn test
```

## Docker

Building the Docker Image

 ```bash
    docker build -t <image name> .
```

Pulling the docker Image

 ```bash
    docker pull djhovi/my-java-app:latest

```

Running the docker Image

 ```bash
    docker run -p8080:8080 djhovi/my-java-app:latest

```