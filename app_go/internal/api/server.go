package api

import (
	"fmt"
	"strconv"
	"time"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/adaptor"
	"github.com/prometheus/client_golang/prometheus/promhttp"
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
func (s *Server) Init(app *fiber.App, m *Metrics) error {
	moscowLocation, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		return fmt.Errorf("failed to load location: %w", err)
	}

	app.Get("/", func(ctx *fiber.Ctx) error {
		log.Info().Msgf("new request from %s", ctx.IP())

		tNow := time.Now()
		response := GetCurrentTimeResponse{
			Time: s.ClockService.GetCurrentTime(moscowLocation).Format(time.RFC3339),
		}

		path := ctx.Path()
		statusCode := strconv.FormatInt(fiber.StatusOK, 10)
		m.HttpRequestDuration.WithLabelValues(path, statusCode).Observe(time.Since(tNow).Seconds())
		m.HttpResponseStatus.WithLabelValues(statusCode).Inc()
		m.HttpRequestNum.WithLabelValues(path).Inc()

		return ctx.JSON(response)
	})

	app.Get("/metrics", adaptor.HTTPHandler(promhttp.Handler()))

	return nil
}
