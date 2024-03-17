package api

import (
	"fmt"
	"time"

	"github.com/gofiber/fiber/v2"
	"github.com/rs/zerolog/log"
)

type ClockService interface {
	GetCurrentTime(location *time.Location) time.Time
}

// Server the server
type Server struct {
	ClockService ClockService
}

// NewServer returns the server
func NewServer(clock ClockService) *Server {
	return &Server{ClockService: clock}
}

// Init will set up the application - routing
func (s *Server) Init(app *fiber.App) error {
	moscowLocation, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		return fmt.Errorf("failed to load location: %w", err)
	}

	app.Get("/", func(ctx *fiber.Ctx) error {
		log.Info().Msgf("new request from %s", ctx.IP())
		return ctx.JSON(GetCurrentTimeResponse{
			Time: s.ClockService.GetCurrentTime(moscowLocation).Format(time.RFC3339),
		})
	})

	return nil
}
