package main

import (
	"github.com/gin-gonic/gin"
	"time"
	"fmt"
	"net/http"
)

func main()  {
	server := gin.Default()
	server.LoadHTMLFiles("index.html")
	
	server.GET("/", func(c *gin.Context) {
		c.HTML(
			http.StatusOK,
			"index.html",
			gin.H{},
		)
	})

	server.GET("/time", func(c *gin.Context){
		loc, _ := time.LoadLocation("Europe/Moscow")
		now := time.Now().In(loc)
		c.JSON(200, gin.H{
			"time": fmt.Sprintf("%2d:%2d:%2d", now.Hour(), now.Minute(), now.Second()),
		})
	})
	server.Run()
}