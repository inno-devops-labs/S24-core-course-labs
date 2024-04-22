package main

import (
	"sync/atomic"
	"encoding/binary"
	"errors"
	"path/filepath"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

const visitsFile = "persistent/visits.bin"
var visits atomic.Uint64

func indexHandler(w http.ResponseWriter, r *http.Request) {
	fact, err := catFact()
	if err == nil {
        w.WriteHeader(http.StatusOK)
		_, _ = fmt.Fprintf(w, "%s", fact)
	} else {
        w.WriteHeader(http.StatusInternalServerError)
		_, _ = fmt.Fprintf(w, "Failed to query a cat fact :(")
	}
}

func visitsHandler(w http.ResponseWriter, r *http.Request) {
	_, _ = fmt.Fprintf(w, "%d", visits.Load())
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

func countVisitsMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		visits.Add(1)	// Atomic increment, no race condition here, so counter
						// is always correct
		buf := make([]byte, binary.MaxVarintLen64)
		binary.LittleEndian.PutUint64(buf, visits.Load())
		// Race condition in the order in which threads will write the file out,
		// so the file may not be correct, but as the same number of bytes is
		// always written out, the counter in the file remains a valid number.
		os.WriteFile(visitsFile, buf, 0644)
		next.ServeHTTP(w, r)
	})
}


func init() {
	_ = os.MkdirAll(filepath.Dir(visitsFile), 0755)
	buf, err := os.ReadFile(visitsFile)
	if err == nil {
		visits.Store(binary.LittleEndian.Uint64(buf))
	} else if errors.Is(err, os.ErrNotExist) {
		visits.Store(0)
	} else {
		panic(err)
	}
}


func main() {
	businessLogic := http.NewServeMux()
	businessLogic.Handle("/", asHandler(indexHandler))
	businessLogic.Handle("/visits", asHandler(visitsHandler))
	// Note: keeping /metrics under middleware too for consistency with app_py
	businessLogic.Handle("/metrics", promhttp.Handler())

	wrapped := noteTimeMiddleware(countVisitsMiddleware(businessLogic))

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
