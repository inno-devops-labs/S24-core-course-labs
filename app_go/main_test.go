package main

import (
    "io"
    "testing"
    "net/http"
    "net/http/httptest"
    "strings"
)

// TestFactLoads tests that the handler returns something that
// is neither empty nor an error
func TestFactLoads(t *testing.T) {
    w := httptest.NewRecorder()

    indexHandler(w, nil)
    resp := w.Result()

    if resp.StatusCode != http.StatusOK {
        t.Fatal("Server responded with exit code", w.Code)
    }

    buf, err := io.ReadAll(w.Body)
    body := string(buf)
    if err != nil {
        t.Fatal("Failed to read response body")
    }
    if len(buf) == 0 {
        t.Fatal("Response body is empty")
    }
    if strings.Contains(body, "Fail") && strings.Contains(body, ":(") {
        t.Fatal("An error occurred while retreiving cat fact")
    }
}
