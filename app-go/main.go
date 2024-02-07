package main

import (
	"fmt"
	"html/template"
	"net/http"
)

var templates = template.Must(template.ParseGlob("templates/*.html"))

func indexHandler(w http.ResponseWriter, r *http.Request) {
	message := "Hello, this is your bonus web application!"
	err := templates.ExecuteTemplate(w, "index.html", message)
	if err != nil {
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}
}

func main() {
	http.HandleFunc("/", indexHandler)
	fmt.Println("Server running on port 8080")
	http.ListenAndServe(":8080", nil)
}
