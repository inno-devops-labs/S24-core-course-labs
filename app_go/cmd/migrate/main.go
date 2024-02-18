package main

import (
	"github.com/Legolass322/example_app_go/internal/config"
	"github.com/Legolass322/example_app_go/internal/db"
	"github.com/Legolass322/example_app_go/internal/logger"
)

func main() {
	cfg := config.MustNewConfig()
	log := logger.New(cfg.Env)

	database := db.MustInit(log, cfg)

	database.MustAutoMigrate()
}
