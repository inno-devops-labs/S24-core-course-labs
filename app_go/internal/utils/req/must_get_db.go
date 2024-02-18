package utilsreq

import (
	"log/slog"
	"net/http"

	"github.com/Legolass322/example_app_go/internal/db"
	utilslog "github.com/Legolass322/example_app_go/internal/utils/log"
	"github.com/gin-gonic/gin"
)

func MustGetDB(ctx *gin.Context, log *slog.Logger) *db.Database {
	db, err := db.Get()
	if err != nil {
		log.Error("Does not have database instance", utilslog.SlogErrWrapper(err))
		ctx.JSON(http.StatusInternalServerError, gin.H{"error": "Internal Error"})
		return nil
	}
	return db
}