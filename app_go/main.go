package main

import (
	"html/template"
	"log"
	"net/http"
	"os"
	"time"
)

type Page struct {
	Time    string
	Picture string
}

func viewHandler(w http.ResponseWriter, r *http.Request) {
	loc, _ := time.LoadLocation("Europe/Moscow")

	// Get the current time and set timezone
	timeString := time.Now().In(loc).Format("2006-01-02 15:04:05")

	logger := log.New(os.Stdout, "INFO: ", log.Ldate|log.Ltime)

	logger.Println("time in Moscow:" + timeString)

	var pictureURL string

	// Determine the time of day
	hour := time.Now().In(loc).Hour()
	if hour >= 6 && hour < 12 {
		pictureURL = "https://i.pinimg.com/564x/51/f3/0e/51f30ef592d831d32a3e99a328a7adb3.jpg"
	} else if hour >= 12 && hour < 18 {
		pictureURL = "https://i.pinimg.com/564x/14/95/70/1495707396edca98a757b584f6609d3f.jpg"
	} else {
		pictureURL = "https://i.pinimg.com/564x/a8/55/66/a85566789478cb55fc3a66aed401b71b.jpg"
	}

	p := &Page{
		Time:    timeString,
		Picture: pictureURL,
	}

	renderTemplate(w, "view", p)
}

var templates = template.Must(template.ParseFiles("view.html"))

func renderTemplate(w http.ResponseWriter, tmpl string, p *Page) {
	err := templates.ExecuteTemplate(w, tmpl+".html", p)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func main() {
	http.HandleFunc("/view/", viewHandler)

	log.Fatal(http.ListenAndServe(":8080", nil))
}
