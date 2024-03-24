package main

import (
 "fmt"
 "log"
 "net/http"
 "os"
 "time"

 "github.com/go-chi/chi"
 "github.com/prometheus/client_golang/prometheus"
 "github.com/prometheus/client_golang/prometheus/promhttp"
)

// Create a new counter vector metric to count the number of times the getTimeHandler is hit
var getTimeCounterVec = prometheus.NewCounterVec(
 prometheus.CounterOpts{
  Namespace: "app",
  Subsystem: "get_time",
  Name:      "requests_total",
  Help:      "Total number of get time requests by status code.",
 },
 []string{"code"},
)

func init() {
 // Register the metric with Prometheus
 prometheus.MustRegister(getTimeCounterVec)
}

func getTimeHandler(w http.ResponseWriter, r *http.Request) {
 // Set the timezone to Moscow
 location, err := time.LoadLocation("Europe/Moscow")
 if err != nil {
  log.Printf("Error retrieving Moscow location: %v\n", err)
  getTimeCounterVec.WithLabelValues("500").Inc() // Increment the counter for status code 500
  http.Error(w, err.Error(), http.StatusInternalServerError)
  return
 }

 // Get the current time in Moscow timezone
 currentTime := time.Now().In(location)
 response := fmt.Sprintf("Current time in Moscow: %s", currentTime.Format("15:04:05"))
 fmt.Fprint(w, response)
 log.Println("Time in Moscow served:", response)
 getTimeCounterVec.WithLabelValues("200").Inc() // Increment the counter for status code 200
}

// setupRouter now also sets up a route for Prometheus metrics at /metrics
func setupRouter() http.Handler {
 r := chi.NewRouter()
 r.Get("/", getTimeHandler)
 r.Handle("/metrics", promhttp.Handler())
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