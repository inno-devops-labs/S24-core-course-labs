package main

import (
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func index(w http.ResponseWriter, r *http.Request) {
	fact, err := catFact()
	if err == nil {
        w.WriteHeader(http.StatusOK)
		_, _ = fmt.Fprintf(w, "%s", fact)
	} else {
        w.WriteHeader(http.StatusInternalServerError)
		_, _ = fmt.Fprintf(w, "Failed to query a cat fact :(")
	}
}


var (
	reqCnt = promauto.NewCounter(prometheus.CounterOpts{
		Name: "go_requests_count",
		Help: "Number of HTTP requests",
	})

	reqHandleTime = promauto.NewHistogram(prometheus.HistogramOpts{
		Name: "go_request_handle_time",
		Help: "Time to handle a request",
	})
)

func noteTimeMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		defer func() {
			var dtSec float64 = time.Since(start).Seconds()
			reqCnt.Inc()
			reqHandleTime.Observe(dtSec)
		}()

		next.ServeHTTP(w, r)
	})
}


func main() {
	businessLogic := http.NewServeMux()
	businessLogic.Handle("/", asHandler(index))
	// Note: keeping /metrics under middleware too for consistency with app_py
	businessLogic.Handle("/metrics", promhttp.Handler())

	wrapped := noteTimeMiddleware(businessLogic)

	hostPort := "0.0.0.0:5000"
	_, _ = fmt.Println("Listening on http://" + hostPort)
	log.Fatal(http.ListenAndServe(hostPort, wrapped))
}


type dummyHandler struct {
	handlerFunc func (http.ResponseWriter, *http.Request)
}

func (h dummyHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	h.handlerFunc(w, r)
}

func asHandler(handlerFunc func (http.ResponseWriter, *http.Request)) dummyHandler {
	return dummyHandler{handlerFunc: handlerFunc}
}
