package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
	_ "time/tzdata"
)

func One() int {
	return 1
}

func mskTimeHandler(w http.ResponseWriter, r *http.Request) {
	loc, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		http.Error(w, "Failed to load Moscow timezone", http.StatusInternalServerError)
		return
	}

	timeInMSK := time.Now().In(loc)
	currentTime := timeInMSK.Format("15:04:05")

	fmt.Fprintf(w, "Current time (MSK timezone): %s", currentTime)
}

func main() {
	http.HandleFunc("/msk_timezone", mskTimeHandler)

	fmt.Println("Server listening on port 8080...")
	fmt.Println("http://localhost:8080/msk_timezone")
	if err := http.ListenAndServe("0.0.0.0:8080", nil); err != nil {
		log.Fatal(err)
	}
}
