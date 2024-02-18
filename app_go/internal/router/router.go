package router

import "github.com/gin-gonic/gin"

type Router struct {
	r gin.IRouter
	gin.RouterGroup
}
