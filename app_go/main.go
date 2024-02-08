package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fact, err := catFact()
	if err == nil {
		_, _ = fmt.Fprintf(w, fact)
	} else {
		_, _ = fmt.Fprintf(w, "Failed to query a cat fact :(")
	}
}

func main() {
	http.HandleFunc("/", handler)
	hostPort := "0.0.0.0:5000"
	_, _ = fmt.Println("Listening on http://" + hostPort)
	log.Fatal(http.ListenAndServe(hostPort, nil))
}
