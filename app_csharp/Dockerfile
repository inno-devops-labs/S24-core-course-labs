FROM mcr.microsoft.com/dotnet/sdk:8.0.200-alpine3.18 AS build
WORKDIR /source

# copy and build
COPY . .
RUN dotnet publish -o /app


# final stage/image
FROM mcr.microsoft.com/dotnet/aspnet:8.0.2-alpine3.18
ENV ASPNETCORE_URLS "http://0.0.0.0:7273"
WORKDIR /app

# Required for Time Zone database lookups
RUN apk add --no-cache tzdata=2024a-r0

COPY --from=build /app .
USER $APP_UID
ENTRYPOINT ["dotnet", "./Web.dll"]