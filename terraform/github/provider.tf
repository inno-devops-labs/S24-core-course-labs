provider "github" {
  token = var.github_token != "" ? var.github_token : getenv("GITHUB_TOKEN")
}
