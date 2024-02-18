package api

import (
	api_v1 "github.com/Legolass322/example_app_go/internal/app/server/api/v1"
	"github.com/gin-gonic/gin"
)

func Use(r gin.IRouter, path string) {
	api := r.Group(path)
	{
		api_v1.Group(api)
	}
}