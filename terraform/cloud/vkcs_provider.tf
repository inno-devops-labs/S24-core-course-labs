terraform {
  required_providers {
    vkcs = {
      source  = "vk-cs/vkcs"
      version = "~> 0.1.12"
    }
  }
}

provider "vkcs" {
  username   = var.vk_login
  password   = var.vk_password
  project_id = "d160a424c7984ed4bf969255b0e3564f"
  region     = "RegionOne"
  auth_url   = "https://infra.mail.ru:35357/v3/"
}
