package utilsreq

import (
	"log/slog"
	"net/http"

	utilslog "github.com/Legolass322/example_app_go/internal/utils/log"
	"github.com/gin-gonic/gin"
	"github.com/gin-gonic/gin/binding"
)

func BindBodyWithJson(ctx *gin.Context, log *slog.Logger, obj any) (ok bool) {
	if err := ctx.ShouldBindBodyWith(obj, binding.JSON); err != nil {
		log.Info("Bad request", utilslog.SlogErrWrapper(err))
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return false
	}
	return true
}
