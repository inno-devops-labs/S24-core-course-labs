package api_v1

import (
	api_v1_records "github.com/Legolass322/example_app_go/internal/app/server/api/v1/records"
	"github.com/gin-gonic/gin"
)

func Group(r *gin.RouterGroup) *gin.RouterGroup {
	v1 := r.Group("/v1")
	{
		api_v1_records.Group(v1)
	}

	return v1
}