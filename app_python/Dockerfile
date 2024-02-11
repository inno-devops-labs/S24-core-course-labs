# start by pulling the python image
FROM python:3.9.18-alpine3.19

# switch working directory
WORKDIR /app

# create user
RUN adduser -D user && chown -R user /app
USER user

# copy every content from the local file to the image
COPY . /app

# install the dependencies and packages in the requirements file (avoid caching)
RUN pip install --no-cache-dir -r requirements.txt

# which port to expose during startup
EXPOSE 5000

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]
