package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

var jokes = []string{
	"Why don't scientists trust atoms? Because they make up everything!",
	"What did one hat say to the other? Stay here, I'm going on ahead!",
	"I told my wife she should embrace her mistakes. She gave me a hug.",
	"Why did the scarecrow win an award? Because he was outstanding in his field!",
	"Parallel lines have so much in common. It's a shame they'll never meet.",
	"I only know 25 letters of the alphabet. I don't know y.",
}

func getMoscowTime() string {
	moscowLocation := time.FixedZone("MSK", 3*60*60) // Moscow is UTC+3
	currentTime := time.Now().In(moscowLocation)
	return currentTime.Format("2006-01-02 15:04:05")
}

func randomJokeHandler(c *gin.Context) {
	randomIndex := rand.Intn(len(jokes))
	randomJoke := jokes[randomIndex]

	c.HTML(http.StatusOK, "index.html", gin.H{"RandomJoke": randomJoke})
}

func main() {
	router := gin.Default()

	router.LoadHTMLGlob("templates/*")
	router.GET("/", randomJokeHandler)

	serverAddr := ":8080"
	fmt.Printf("Server is running on http://127.0.0.1%s\n", serverAddr)

	if err := router.Run(serverAddr); err != nil {
		fmt.Printf("Error starting the server: %v\n", err)
	}
}
