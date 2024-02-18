package app

import (
	"log/slog"
	"os"
	"os/signal"
	"syscall"

	app_server "github.com/Legolass322/example_app_go/internal/app/server"
	"github.com/Legolass322/example_app_go/internal/config"
	"github.com/Legolass322/example_app_go/internal/db"
)

type App struct {
	server   *app_server.Server
	database *db.Database
	log      *slog.Logger
	cfg      *config.Config
}

func New(log *slog.Logger, cfg *config.Config) *App {
	database := db.MustInit(log, cfg)
	server := app_server.New(log, cfg)

	return &App{
		server,
		database,
		log,
		cfg,
	}
}

func (a *App) MustStart() {
	a.server.MustRun()
}

func (a *App) Stop() {
	stop := make(chan os.Signal, 1)
	signal.Notify(stop, syscall.SIGTERM, syscall.SIGINT)
	signalStop := <-stop

	a.log.Info("Interrupted by", slog.String("signal", signalStop.String()))

	a.server.Stop()

	a.log.Info("Stopped")
}
