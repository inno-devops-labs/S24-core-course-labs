package api_v1_records

import (
	api_v1_records_v1 "github.com/Legolass322/example_app_go/internal/app/server/api/v1/records/v1"
	"github.com/gin-gonic/gin"
)

func Group(r *gin.RouterGroup) *gin.RouterGroup {
	records := r.Group("/records")
	{
		api_v1_records_v1.Group(records)
	}

	return records
}