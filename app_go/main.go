package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fact, err := catFact()
	if err == nil {
        w.WriteHeader(http.StatusOK)
		_, _ = fmt.Fprintf(w, "%s", fact)
	} else {
        w.WriteHeader(http.StatusInternalServerError)
		_, _ = fmt.Fprintf(w, "Failed to query a cat fact :(")
	}
}

func main() {
	http.HandleFunc("/", handler)
	hostPort := "0.0.0.0:5000"
	_, _ = fmt.Println("Listening on http://" + hostPort)
	log.Fatal(http.ListenAndServe(hostPort, nil))
}
