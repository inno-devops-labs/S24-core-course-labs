package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strconv"
	"time"
)

func main() {
	http.HandleFunc("/", moscowTimeResponder)
	http.HandleFunc("/visits", visitsResponder)
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

	visits, err := ioutil.ReadFile("./volume/visits")
	if err != nil {
		http.Error(response, err.Error(), http.StatusInternalServerError)
		return
	}
	visitsInt, err := strconv.Atoi(string(visits))
	if err != nil {
		http.Error(response, err.Error(), http.StatusInternalServerError)
		return
	}
	visitsInt++
	visits = []byte(strconv.Itoa(visitsInt))
	err = ioutil.WriteFile("./volume/visits", visits, 0644)
	if err != nil {
		http.Error(response, err.Error(), http.StatusInternalServerError)
		return
	}
}

func visitsResponder(w http.ResponseWriter, r *http.Request) {
	// Read the file "./volume/visits"
	visits, err := ioutil.ReadFile("./volume/visits")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Write the number of visits to the HTTP response
	fmt.Fprintf(w, "Number of visits: %s\n", visits)
}
