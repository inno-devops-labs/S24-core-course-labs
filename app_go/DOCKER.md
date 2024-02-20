# Docker best practices

I implemented some docker best practices, such as:
- Copy necessary files only
- I preferred COPY over ADD
- I used rootless docker container
- I used specific version of image, so there won't be unnecessary pulling
- I used multistage build to reduce the resulting image size
