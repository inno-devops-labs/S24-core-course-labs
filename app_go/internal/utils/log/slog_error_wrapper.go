package utilslog

import "log/slog"

func SlogErrWrapper(e error) slog.Attr {
	return slog.String("err", e.Error())
}