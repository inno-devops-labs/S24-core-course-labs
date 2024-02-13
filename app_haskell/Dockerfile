FROM haskell:9.2.8-slim-buster AS build
WORKDIR /app

COPY app-haskell.cabal package.yaml stack.yaml stack.yaml.lock ./
RUN stack build --verbose --system-ghc --only-dependencies

COPY . .
RUN stack build --verbose --system-ghc --copy-bins

FROM debian:buster-slim
WORKDIR /app

RUN useradd app && chown -R app /app
COPY --from=build /root/.local/bin/app-haskell-exe exe

USER app
CMD ["/app/exe"]
EXPOSE 8081
