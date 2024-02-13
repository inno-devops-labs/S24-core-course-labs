FROM mcr.microsoft.com/dotnet/aspnet:7.0.11-alpine3.18 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:7.0.401-alpine3.18 AS build
WORKDIR /src
COPY ["MoscowTime.csproj", "./"]
RUN dotnet restore "MoscowTime.csproj"
COPY . .
WORKDIR "/src/"
RUN dotnet build "MoscowTime.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "MoscowTime.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .

RUN adduser app --system -D
USER app

ENTRYPOINT ["dotnet", "MoscowTime.dll"]
