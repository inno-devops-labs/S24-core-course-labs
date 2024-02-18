package middlewares

import (
	"github.com/Legolass322/example_app_go/internal/config"
	"github.com/gin-gonic/gin"
)

const config_field_name = "config"

func Config(cfg *config.Config) gin.HandlerFunc {
	return func(ctx *gin.Context) {
		ctx.Set(config_field_name, cfg)

		ctx.Next()
	}
}

func ExtractConfig(ctx *gin.Context) *config.Config {
	return ctx.MustGet(config_field_name).(*config.Config)
}