FROM python:3-alpine3.15

# Add a group and add an user
RUN addgroup -S appgroup
RUN adduser -S appuser -G appgroup
USER appuser

ENV PATH /home/appuser/.local/bin:${PATH}

# Set the working directory to /app
WORKDIR /app

# Copy only 2 files contents into the directory for caching
COPY ./requirements.txt ./requirements.txt
COPY ./templates ./templates/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Flask
RUN pip install Flask

# Copy all the contents
COPY ./app.py .

# expose the port 5555 for interaction
EXPOSE 5555

# Run app.py 
CMD ["flask", "run", "--host=0.0.0.0", "--port=5555"]