package main

import (
    "fmt"
    "net/http"
    "time"
)

func handler(w http.ResponseWriter, r *http.Request) {
    moscowTime := time.Now().UTC().Add(time.Hour * 3)
    fmt.Fprintf(w, "Current time in Moscow: %s", moscowTime.Format("15:04:05"))
}

func main() {
    http.HandleFunc("/", handler)
    fmt.Println("Server is running on port 8000")
    http.ListenAndServe(":8000", nil)
}

