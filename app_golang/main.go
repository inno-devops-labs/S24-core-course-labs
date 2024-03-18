package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"time"
)

func mskTime(w http.ResponseWriter, r *http.Request) {
	loc, _ := time.LoadLocation("Europe/Moscow")
	log.Println("Server was started")
	timeInMSK := time.Now().In(loc)
	currentTimeMsk := timeInMSK.Format("15:04:05")

	fmt.Fprintf(w, "Current time: %s", currentTimeMsk)
	log.Println("Time in Moscow served:", currentTimeMsk)
}

func main() {
	logFile, err := os.OpenFile("/app/logs/server.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err != nil {
		log.Fatal("Error opening log file:", err)
	}
	defer logFile.Close()

	// Direct log output to file and stdout
	log.SetOutput(logFile)
	log.SetOutput(os.Stdout)

	// Log server start
	log.Println("Starting server on port 8081")

	http.HandleFunc("/msk_time", mskTime)
	http.ListenAndServe(":8080", nil)
}
