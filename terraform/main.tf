module "app_python" {
  source = "./docker"

  image          = "adarika/devops-lab-02-python"
  container_name = "python_app"
}

module "yandex_cloud" {
  source           = "./yandex_cloud"
  vm_name          = "devops-lab"
  service_token = ""
}

module "github" {
  source = "./github"
  token     = ""
}

module "github_teams" {
  source = "./github_teams"

  github_organization = "intaby"
  token               = "" 
  repository          = "devops-repo"
}