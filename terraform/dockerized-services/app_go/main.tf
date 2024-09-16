resource "docker_image" "pg" {
  name = "postgres:latest"
}

resource "docker_image" "app_go" {
  name = "legolass322/devops:app_go"
}

resource "docker_network" "net" {
  name = "devops_network"
}

resource "docker_container" "app_go" {
  image = docker_image.app_go.image_id
  depends_on = [docker_container.pg]
  name  = var.container_name
  ports {
    internal = var.SERVER_PORT
    external = var.external_port
  }
  env = [
    local.ENV_PG_DBNAME,
    local.ENV_PG_PASSWORD,
    local.ENV_PG_USER,
    local.ENV_SERVER_HOST,
    local.ENV_SERVER_PORT,
    "DB_HOST=database",
    local.ENV_ENV
  ]
  networks_advanced {
    name = docker_network.net.id
  }
}

resource "docker_container" "pg" {
  image = docker_image.pg.image_id
  name  = var.container_pg_name
  ports {
    internal = 5432
    external = var.external_pg_port
  }
  env = [local.ENV_PG_DBNAME, local.ENV_PG_PASSWORD, local.ENV_PG_USER]
  networks_advanced {
    name = docker_network.net.id
  }
  hostname = "database"
}
