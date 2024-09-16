package config

type Env int8

const (
	Local Env = iota + 1
	Testing
	Production
)

func (env Env) String() string {
	switch env {
	case Local:
		return "local"
	case Testing:
		return "testing"
	case Production:
		return "production"
	}
	return "undefined"
}

func fromString(str string) Env {
	switch str {
	case "local":
		return Local
	case "testing":
		return Testing
	case "production":
		return Production
	}
	return 0
}
