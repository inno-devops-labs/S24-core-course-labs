package app_server

import (
	"context"
	"errors"
	"fmt"
	"log/slog"
	"net/http"

	"github.com/Legolass322/example_app_go/internal/app/server/api"
	"github.com/Legolass322/example_app_go/internal/app/server/middlewares"
	"github.com/Legolass322/example_app_go/internal/app/server/pages"
	"github.com/Legolass322/example_app_go/internal/config"
	utilslog "github.com/Legolass322/example_app_go/internal/utils/log"
	"github.com/gin-gonic/gin"
)

type Server struct {
	log    *slog.Logger
	cfg    *config.Config
	server *http.Server
}

func New(log *slog.Logger, cfg *config.Config) *Server {
	router := gin.Default() // todo: provide custom logger

	router.Use(middlewares.Logger(log))
	router.Use(middlewares.Config(cfg))
	api.Use(router, "/api")
	pages.Use(router)

	server := &http.Server{
		Addr:         fmt.Sprintf("%v:%d", cfg.ServerCfg.Host, cfg.ServerCfg.Port),
		Handler:      router,
		ReadTimeout:  cfg.ServerCfg.Timeout,
		WriteTimeout: cfg.ServerCfg.Timeout,
	}

	return &Server{log, cfg, server}
}

func (app *Server) MustRun() {
	if err := app.Run(); err != nil && !errors.Is(err, http.ErrServerClosed) {
		panic(fmt.Errorf("Couldn't run: %w", err))
	}
}

func (app *Server) Run() error {
	const op = "app.server.Run"

	log := app.log.With(utilslog.SlogOpWrapper(op))

	log.Info("Starting server...")

	return app.server.ListenAndServe()
}

func (app *Server) Stop() {
	const op = "app.server.Stop"

	log := app.log.With(utilslog.SlogOpWrapper(op))

	log.Info("Stopping server...")

	ctx, cancel := context.WithTimeout(context.Background(), app.cfg.ServerCfg.GracefulStopTimeout)
	defer cancel()
	if err := app.server.Shutdown(ctx); err != nil {
		log.Error("Server shutdown:", err)
	}

	select {
	case <-ctx.Done():
		log.Warn("Timeout on shutdown")
	}
	log.Info("Server stopped")
}
