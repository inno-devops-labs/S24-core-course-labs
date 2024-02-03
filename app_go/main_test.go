package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

func TestTimeChanges(t *testing.T) {
	// Create a request to the /view/ endpoint (adjust as needed)
	req, err := http.NewRequest("GET", "/view/", nil)
	if err != nil {
		t.Fatal(err)
	}

	// Create a ResponseRecorder to record the response
	rr := httptest.NewRecorder()

	// Create a test server with the viewHandler as the handler
	handler := http.HandlerFunc(viewHandler)

	// Serve the request to the test server and record the first response
	handler.ServeHTTP(rr, req)
	responseA := rr.Body.String()

	// Wait for a short duration (e.g., 1 second)
	time.Sleep(1 * time.Second)

	// Serve the same request again to the test server and record the second response
	rr = httptest.NewRecorder()
	handler.ServeHTTP(rr, req)
	responseB := rr.Body.String()

	// Check if the responses are not equal
	if responseA == responseB {
		t.Errorf("expected response to change over time, but got the same response: %v", responseA)
	}
}
