FROM python:3.9-alpine

# Create a non-root user and switch to it
RUN adduser -D userwithoutroot
USER userwithoutroot

# Set up the working directory and copy only what's needed
WORKDIR /home/userwithoutroot/app
COPY --chown=userwithoutroot:userwithoutroot requirements.txt app.py ./
COPY --chown=userwithoutroot:userwithoutroot templates ./templates/

# Install app dependencies
RUN pip install --user -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run Flask as non-root user
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]