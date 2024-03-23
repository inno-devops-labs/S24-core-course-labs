package api

import (
	"github.com/prometheus/client_golang/prometheus"
)

type Metrics struct {
	HttpRequestNum      *prometheus.CounterVec
	HttpResponseStatus  *prometheus.CounterVec
	HttpRequestDuration *prometheus.HistogramVec
}

func NewMetrics() *Metrics {
	return &Metrics{
		HttpRequestNum: prometheus.NewCounterVec(
			prometheus.CounterOpts{
				Namespace: "app",
				Name:      "http_requests_total",
				Help:      "Number of requests",
			},
			[]string{"path"},
		),
		HttpRequestDuration: prometheus.NewHistogramVec(
			prometheus.HistogramOpts{
				Namespace: "app",
				Name:      "http_response_time_seconds",
				Help:      "Duration of HTTP requests.",
				Buckets:   []float64{0.1, 0.15, 0.2, 0.25, 0.3, 1, 3, 5},
			}, []string{"path", "status_code"}),
		HttpResponseStatus: prometheus.NewCounterVec(
			prometheus.CounterOpts{
				Namespace: "app",
				Name:      "http_response_status",
				Help:      "Status code of HTTP response",
			},
			[]string{"status_code"},
		),
	}
}

func (m *Metrics) Register() error {
	if err := prometheus.Register(m.HttpResponseStatus); err != nil {
		return err
	}

	if err := prometheus.Register(m.HttpRequestNum); err != nil {
		return err
	}

	if err := prometheus.Register(m.HttpRequestDuration); err != nil {
		return err
	}
	return nil
}
