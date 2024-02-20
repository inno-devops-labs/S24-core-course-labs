FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base

RUN groupadd -r appgroup && useradd -r -g appgroup -m -s /bin/bash appuser

WORKDIR /
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
COPY ["app_dotnet/app_dotnet.csproj", "app_dotnet/"]
RUN dotnet restore "app_dotnet/app_dotnet.csproj"
COPY ./app_dotnet ./app_dotnet
WORKDIR "/app_dotnet"
RUN dotnet build "app_dotnet.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "app_dotnet.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "app_dotnet.dll"]
