FROM python:3.9-slim

# set the working directory
WORKDIR /app

COPY requirements.txt requirements.txt

# Create user
RUN useradd user -m 

RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R user:user /app

# switch to the user
USER user

# copy after starting installing the requirements
COPY app.py app.py
COPY test_app.py test_app.py

# Expose the port
EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]