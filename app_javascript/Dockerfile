FROM node:20-alpine3.18 AS base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable pnpm
COPY . /app
WORKDIR /app

FROM base AS prod-deps
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --prod --frozen-lockfile

FROM base AS build
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
RUN pnpm run build

FROM base

# Use non-root user
USER node

COPY --from=prod-deps /app/node_modules /app/node_modules
COPY --from=build /app/public /app/public

EXPOSE 8000

CMD [ "pnpm", "start", "--host", "--port=8000" ]
