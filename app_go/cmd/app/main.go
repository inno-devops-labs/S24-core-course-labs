package main

import (
	"os"
	"os/signal"
	"syscall"
	"time"

	"app_go/internal/api"
	"app_go/internal/service"

	"github.com/gofiber/fiber/v2"
	"github.com/rs/zerolog/log"
)

func main() {
	// metrics
	m := api.NewMetrics()
	if err := m.Register(); err != nil {
		log.Fatal().Err(err).Msg("failed to init metrics")
	}

	// clock service
	clockService := service.NewClock(time.Now)

	// Setting up the server
	addr := os.Getenv("ADDR")
	if addr == "" {
		addr = "0.0.0.0:8080"
	}

	// Starting the server
	server := api.NewServer(clockService)
	go func() {
		log.Info().Msg("starting the web server on addr:" + addr)
		app := fiber.New()
		if err := server.Init(app, m); err != nil {
			log.Fatal().Err(err).Msg("failed to init the server")
		}

		if err := app.Listen(addr); err != nil {
			log.Fatal().Err(err).Msg("failed to run the server")
		}
	}()

	// gracefully shutdown
	signalCh := make(chan os.Signal, 1)
	signal.Notify(signalCh, syscall.SIGTERM, syscall.SIGINT)
	<-signalCh
	log.Info().Msg("gracefully shutdown")
}
