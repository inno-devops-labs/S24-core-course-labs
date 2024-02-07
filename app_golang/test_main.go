package main

import (
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"
)

func TestMoscowTimeResponder(t *testing.T) {
	// Create a new HTTP server for testing purposes
	ts := httptest.NewServer(http.HandlerFunc(moscowTimeResponder))
	defer ts.Close()

	// Make a request to our test server
	resp, err := http.Get(ts.URL)
	if err != nil {
		t.Fatalf("Failed to make request: %s", err)
	}
	defer resp.Body.Close()

	// Read the response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		t.Fatalf("Failed to read response body: %s", err)
	}

	// Check if the response body contains a time string
	// Note: This is a basic check and might need to be adjusted based on how you format the time string.
	if !strings.Contains(string(body), "Moscow Time Now:") {
		t.Errorf("Expected response to contain 'Moscow Time Now:', got %s", body)
	}
}
