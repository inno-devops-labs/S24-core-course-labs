package main

import (
	"os"

	"github.com/Legolass322/example_app_go/internal/app"
	"github.com/Legolass322/example_app_go/internal/config"
	"github.com/Legolass322/example_app_go/internal/logger"
)

func main() {
	cfg := config.MustNewConfig()
	log := logger.New(cfg.Env)

	application := app.New(log, cfg)

	go application.MustStart()
	application.Stop()

	os.Exit(0)
}
