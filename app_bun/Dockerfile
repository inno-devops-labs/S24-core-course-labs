# use the official Bun image
# see all versions at https://hub.docker.com/r/oven/bun/tags
FROM oven/bun:1@sha256:ce1b800a070f3a11330a344801d49980854de2e346e344e793d472e71c18581d as base

LABEL description="This is a simple bun app" maintainer="pptx704"

WORKDIR /app/app_bun
RUN adduser --disabled-password --gecos "" newuser && chown -R newuser /app/app_bun
USER newuser

# install dependencies into temp directory
# this will cache them and speed up future builds
FROM base AS install
RUN mkdir -p /home/newuser/dev
COPY package.json bun.lockb /home/newuser/dev/
RUN cd /home/newuser/dev && bun install --frozen-lockfile

# copy node_modules from dev directory
# then copy ts files for testing and building
FROM base AS prerelease
COPY --from=install /home/newuser/dev/node_modules node_modules
COPY entry.ts utils.ts app.ts app.test.ts ./

# test and build
RUN bun test && bun build ./entry.ts --outdir . --target=bun

# copy production dependencies and source code into final image
FROM base AS release
COPY --from=prerelease /app/app_bun/entry.js .
# run the app
CMD [ "bun", "run", "entry.js" ]