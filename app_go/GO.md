# Time Table app development

## Development

I've decided to run simple web server using [Gin](https://gin-gonic.com/) framework.
It's pretty easy and fast framework for simple web applications.

## Quality

In order to ensure code quality I've integrated `Golang-Lint Github Action` into github repository.

## Readability

- The code were written in the most consise way with proper naming conventions.
- It was properly commented.

## Testing

As a result, application shows time on every page refresh:

![Start Page](assets/pic0.png)

![Reload Page](assets/pic1.png)

## Unit tests

I have written one unit test, which checks for valid time:

```golang
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
```
