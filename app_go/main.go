package main

import (
 "fmt"
 "log"
 "net/http"
 "os"
 "time"

 "github.com/go-chi/chi"
)

func getTimeHandler(w http.ResponseWriter, r *http.Request) {
 // Set the timezone to Moscow
 location, err := time.LoadLocation("Europe/Moscow")
 if err != nil {
  log.Printf("Error retrieving Moscow location: %v\n", err)
  http.Error(w, err.Error(), http.StatusInternalServerError)
  return
 }

 // Get the current time in Moscow timezone
 currentTime := time.Now().In(location)
 response := fmt.Sprintf("Current time in Moscow: %s", currentTime.Format("15:04:05"))
 fmt.Fprint(w, response)
 log.Println("Time in Moscow served:", response)
}

func setupRouter() http.Handler {
 r := chi.NewRouter()
 r.Get("/", getTimeHandler)
 return r
}

func main() {
 // Logging to a file or os.Stdout
 logFile, err := os.OpenFile("/app/logs/server.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
 if err != nil {
  log.Fatal("Error opening log file:", err)
 }
 defer logFile.Close()

 // Direct log output to file and stdout
 log.SetOutput(logFile)
 log.SetOutput(os.Stdout)

 // Set up the router
 router := setupRouter()

 // Log server start
 log.Println("Starting server on port 8081")

 // Start the server on port 8081
 if err := http.ListenAndServe(":8081", router); err != nil {
  log.Fatal("Error starting server:", err)
 }
}