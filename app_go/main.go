package main

import (
 "fmt"
 "io/ioutil"
 "log"
 "net/http"
 "os"
 "strconv"
 "time"

 "github.com/go-chi/chi"
 "github.com/prometheus/client_golang/prometheus"
 "github.com/prometheus/client_golang/prometheus/promhttp"
)

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
 prometheus.MustRegister(getTimeCounterVec)
}

func getTimeHandler(w http.ResponseWriter, r *http.Request) {
 location, err := time.LoadLocation("Europe/Moscow")
 if err != nil {
  log.Printf("Error retrieving Moscow location: %v\n", err)
  getTimeCounterVec.WithLabelValues("500").Inc()
  http.Error(w, err.Error(), http.StatusInternalServerError)
  return
 }

 currentTime := time.Now().In(location)
 response := fmt.Sprintf("Current time in Moscow: %s", currentTime.Format("15:04:05"))
 fmt.Fprint(w, response)
 log.Println("Time in Moscow served:", response)

 counterData, err := ioutil.ReadFile("data/visits.txt")
 if err != nil {
  log.Printf("Error reading counter: %v\n", err)
  return
 }

 counter, err := strconv.Atoi(string(counterData))
 if err != nil {
  log.Printf("Error converting counter to int: %v\n", err)
  return
 }

 counter++
 getTimeCounterVec.WithLabelValues("200").Inc()
 err = ioutil.WriteFile("data/visits.txt", []byte(strconv.Itoa(counter)), 0644)
 if err != nil {
  log.Printf("Error writing counter: %v\n", err)
  return
 }
}

func getVisitsHandler(w http.ResponseWriter, r *http.Request) {
 counterData, err := ioutil.ReadFile("data/visits.txt")
 if err != nil {
  log.Printf("Error reading counter: %v\n", err)
  http.Error(w, "Internal Server Error", http.StatusInternalServerError)
  return
 }
 fmt.Fprint(w, string(counterData))
}

func setupRouter() http.Handler {
 r := chi.NewRouter()
 r.Get("/", getTimeHandler)
 r.Get("/visits", getVisitsHandler)
 r.Handle("/metrics", promhttp.Handler())
 return r
}

func main() {
 logFile, err := os.OpenFile("/app/logs/server.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
 if err != nil {
  log.Fatal("Error opening log file:", err)
 }
 defer logFile.Close()

 log.SetOutput(logFile)
 log.SetOutput(os.Stdout)

 router := setupRouter()

 log.Println("Starting server on port 8081")
 err = ioutil.WriteFile("data/visits.txt", []byte("0"), 0644)
 if err != nil {
  log.Fatal("Error initializing counter file:", err)
 }

 err = http.ListenAndServe(":8081", router)
 if err != nil {
  log.Fatal("Error starting server:", err)
 }
}