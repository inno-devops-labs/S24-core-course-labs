package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Printf("Got request with url: %v\n", r.URL)
}

func main() {

	fs := http.FileServer(http.Dir("static"))

	http.Handle("/", fs)
	http.HandleFunc("/api", handler)

	fmt.Println("Starting server")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Failed to start the server")

	}

}
