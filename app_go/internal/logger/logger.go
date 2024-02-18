package logger

import (
	"log/slog"
	"os"

	"github.com/Legolass322/example_app_go/internal/config"
)

func New(env config.Env) *slog.Logger {
	var log *slog.Logger

	switch env {
	case config.Local:
		log = slog.New(
			slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}),
		)
	case config.Testing:
		log = slog.New(
			slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}),
		)
	case config.Production:
		log = slog.New(
			slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelInfo}),
		)
	}

	return log
}
