module "app_python" {
  source = "./docker"

  image          = "evsey/flask-moscow-time-app"
  container_name = "python_app"
}

module "yandex_cloud" {
  source           = "./yandex_cloud"
  vm_name          = "terraform1"
  service_token = ""
}

module "github" {
  source = "./github"
  token     = ""
}