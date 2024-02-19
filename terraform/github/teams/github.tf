# Existing repository
resource "github_repository" "readme" {
  name        = "TeamOmukk"
  description = "Profile README"
  visibility  = "public"
}

# New repository
resource "github_repository" "mock" {
  name        = "tf-mock"
  description = "This is a mock repository for testing purposes."
  visibility  = "public"
}

# Read-only team
resource "github_team" "reader" {
  name        = "reader"
  description = "This team has read-only access to the repositories."
  privacy = "closed"
}

resource "github_team_members" "reader" {
  team_id = github_team.reader.id

  members {
    username = "pptx704"
    role     = "member"
  }

  members {
    username = "binarysakir"
    role     = "member"
  }
}

# Write team
resource "github_team" "writer" {
  name        = "writer"
  description = "This team has write access to the repositories."
}

resource "github_team_members" "writer" {
  team_id = github_team.writer.id

  members {
    username = "pptx704"
    role     = "member"
  }

  members {
    username = "binarysakir"
    role     = "member"
  }
}

# Mixed team
resource "github_team" "mixed" {
  name        = "mixed"
  description = "This team has different access levels to different repos."
}

resource "github_team_members" "mixed" {
  team_id = github_team.mixed.id

  members {
    username = "pptx704"
    role     = "maintainer"
  }
}

# Assign the teams for jekyll repo
resource "github_repository_collaborators" "jekyll" {
  repository = github_repository.readme.name

  team {
    team_id    = github_team.reader.id
    permission = "pull"
  }

  team {
    team_id    = github_team.writer.id
    permission = "push"
  }

  team {
    team_id    = github_team.mixed.id
    permission = "pull"
  }
}

# Assign the teams for mock repo
resource "github_repository_collaborators" "mock" {
  repository = github_repository.mock.name

  team {
    team_id    = github_team.reader.id
    permission = "pull"
  }

  team {
    team_id    = github_team.writer.id
    permission = "push"
  }

  team {
    team_id    = github_team.mixed.id
    permission = "push"
  }
}