package api_v1_records_v1

import "github.com/gin-gonic/gin"

func Group(r *gin.RouterGroup) *gin.RouterGroup {
	v1 := r.Group("/v1")
	{
		v1.POST("/add", add)
		v1.GET("/list", list)
	}

	return v1
}