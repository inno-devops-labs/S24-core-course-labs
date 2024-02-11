FROM python:3.10-alpine

# Set the working directory to /python_app
WORKDIR /app_python

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user to run the application
RUN adduser -D user && chown -R user /app_python

# Switch to the non-root user
USER user

# Copy the rest of the project to the working directory
COPY  . .

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]