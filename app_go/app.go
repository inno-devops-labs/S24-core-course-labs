package main

import (
	"fmt"
    "io"
    "net/http"
)

// cat handler, get random cat and shows to user
func handler(w http.ResponseWriter, r *http.Request) {
	resp, err := http.Get("https://cataas.com/cat")
	if err != nil {
		http.Error(w, "Unable to fetch image", http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()
	w.Header().Set("Content-Type", "image/png")
	io.Copy(w, resp.Body)
}

// main function that set ups http handlers
func main() {
    http.HandleFunc("/", handler)
	fmt.Println("Starting server at :8080")
    http.ListenAndServe(":8080", nil)
}