package main

import (
	"fmt"
	"net/http"
	"time"
)

func mskTime(w http.ResponseWriter, r *http.Request) {
	loc, _ := time.LoadLocation("Europe/Moscow")

	timeInMSK := time.Now().In(loc)
	currentTimeMsk := timeInMSK.Format("15:04:05")

	fmt.Fprintf(w, "Current time: %s", currentTimeMsk)
}

func main() {
	http.HandleFunc("/msk_time", mskTime)
	http.ListenAndServe(":8080", nil)
}
