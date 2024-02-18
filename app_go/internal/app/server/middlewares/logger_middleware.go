package middlewares

import (
	"log/slog"

	"github.com/gin-gonic/gin"
)

const log_field_name = "log"

func Logger(log *slog.Logger) gin.HandlerFunc {
	return func(ctx *gin.Context) {
		ctx.Set(log_field_name, log)

		ctx.Next()
	}
}

func ExtractLogger(ctx *gin.Context) *slog.Logger {
	return ctx.MustGet(log_field_name).(*slog.Logger)
}