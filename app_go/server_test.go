package main

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"regexp"
	"testing"

	"github.com/stretchr/testify/assert"
)

type Time struct {
	Time string `json:"time"`
}

func TestTimeRoute(t *testing.T) {
	var got Time

	router := setupRouter()

	w := httptest.NewRecorder()
	req, err := http.NewRequest("GET", "/time", nil)
	if err != nil {
		t.Fatal("Failed to send request")
	}
	router.ServeHTTP(w, req)

	assert.Equal(t, 200, w.Code)

	err = json.Unmarshal(w.Body.Bytes(), &got)

	if err != nil {
		t.Fatalf("Failed to get JSON")
	}

	re := regexp.MustCompile(`\d{2}\:\d{2}\:\d{2}`)

	assert.True(t, re.MatchString(got.Time))
}
