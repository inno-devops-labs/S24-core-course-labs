package utilslog

import "log/slog"

func SlogOpWrapper(op string) slog.Attr {
	return slog.String("op", op)
}