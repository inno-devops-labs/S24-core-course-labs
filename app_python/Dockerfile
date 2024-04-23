FROM python:3.9.18-slim-bullseye

# Include metadata
LABEL version="1.0" maintainer="exemplerie@mail.ru"

# Set the working directory
WORKDIR /app

# Create a non-root user
RUN adduser myuser && chown -R myuser /app

# Switch to non-root user
USER myuser

# Copy only the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt --no-cache-dir

# Copy the application files
COPY . /app

RUN mkdir /app/data && touch /app/data/visits.txt

# Expose the application port
EXPOSE 6000

# Set the entry point
CMD [ "python", "-u", "app.py", "--host", "0.0.0.0", "--port", "6000"]