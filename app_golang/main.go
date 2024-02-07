package main

import (
	"net/http"
	"time"
	"fmt"
)

func main() {
	http.HandleFunc("/", moscowTimeResponder)
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Printf("Error starting server: %s\n", err)
	}
}

func moscowTimeResponder(response http.ResponseWriter, request *http.Request) {
	// Configure to use Moscow Time Zone
	moscowTZ, tzError := time.LoadLocation("Europe/Moscow")
	if tzError != nil {
		http.Error(response, tzError.Error(), http.StatusInternalServerError)
		return
	}

	// Obtain and format the Moscow time
	nowInMoscow := time.Now().In(moscowTZ)
	timeFormatted := nowInMoscow.Format("2006-01-02 15:04:05 MST")

	// Respond with the current time in Moscow
	fmt.Fprintf(response, "Moscow Time Now: %s\n", timeFormatted)
}
