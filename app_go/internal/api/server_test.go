package api

import (
	"app_go/internal/service"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/utils"
	"io"
	"net/http/httptest"
	"testing"
	"time"
)

type apiServerSuite struct {
	Server
	app *fiber.App
}

func newTestApiServerSuite(clock ClockService) Server {
	return Server{
		ClockService: clock,
	}
}

func getTestApiServerSuite(t *testing.T, clock ClockService) *apiServerSuite {
	s := &apiServerSuite{
		Server: newTestApiServerSuite(clock),
		app:    fiber.New(),
	}

	if err := s.Init(s.app, NewMetrics()); err != nil {
		t.Fatal(err)
	}

	return s
}

func TestApiServer(t *testing.T) {
	moscowLocation, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		t.Fatalf("failed to load location: %v", err)
	}

	type response struct {
		StatusCode int
		Body       string
	}

	type request struct {
		Target string
		Body   io.Reader
		Method string
	}

	tests := []struct {
		name     string
		request  request
		response response
		nowFunc  func() time.Time
	}{
		{
			request: request{
				Body:   nil,
				Target: "/",
				Method: fiber.MethodGet,
			},
			nowFunc: func() time.Time {
				t := time.Date(2024, 2, 5, 0, 47, 33, 0, moscowLocation)
				return t
			},
			response: response{
				StatusCode: fiber.StatusOK,
				Body:       `{"time":"2024-02-05T00:47:33+03:00"}`,
			},
			name: "'GET /' OK",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			c := service.NewClock(tt.nowFunc)
			s := getTestApiServerSuite(t, c)

			req := httptest.NewRequest(tt.request.Method, tt.request.Target, tt.request.Body)
			resp, err := s.app.Test(req)
			if err != nil {
				t.Error(err)
				t.Fail()
				return
			}

			defer resp.Body.Close()
			respBody, err := io.ReadAll(resp.Body)
			if err != nil {
				t.Error(err)
				t.Fail()
				return
			}

			utils.AssertEqual(t, err, nil, "request error")
			utils.AssertEqual(t, tt.response.StatusCode, resp.StatusCode, "response status code")
			utils.AssertEqual(t, tt.response.Body, string(respBody), "response body")
		})
	}
}
