package pages

import (
	"encoding/json"
	"net/http"

	"github.com/Legolass322/example_app_go/internal/app/server/middlewares"
	utilslog "github.com/Legolass322/example_app_go/internal/utils/log"
	utilsreq "github.com/Legolass322/example_app_go/internal/utils/req"
	"github.com/gin-gonic/gin"
)

func Use(r *gin.Engine) {
	r.LoadHTMLGlob("templates/*")

	r.GET("/", func(ctx *gin.Context) {
		const op = "pages:/"
		log := middlewares.ExtractLogger(ctx).With(utilslog.SlogOpWrapper(op))

		db := utilsreq.MustGetDB(ctx, log)
		if db == nil {
			return
		}

		records, err := db.ListRecords()
		if err != nil {
			log.Error("Cannot write db", utilslog.SlogErrWrapper(err))
			utilsreq.InternalError(ctx)
			return
		}

		recordsByteJson, err := json.Marshal(records)
		if err != nil {
			log.Error("Cannot marshal records", utilslog.SlogErrWrapper(err))
			utilsreq.InternalError(ctx)
			return
		}

		nBytes := len(recordsByteJson)
		recordsJson := string(recordsByteJson[:nBytes])

		ctx.HTML(http.StatusOK, "index.html", gin.H{
			"records": recordsJson,
		})
	})
}
