package api_v1_records_v1

import (
	"net/http"

	"github.com/Legolass322/example_app_go/internal/app/server/middlewares"
	utilslog "github.com/Legolass322/example_app_go/internal/utils/log"
	utilsreq "github.com/Legolass322/example_app_go/internal/utils/req"
	"github.com/gin-gonic/gin"
)

type addRecordRequest struct {
	Text string `json:"text" binding:"required"`
}

func add(ctx *gin.Context) {
	const op = "handler:/api/v1/records/v1/add"
	log := middlewares.ExtractLogger(ctx).With(utilslog.SlogOpWrapper(op))

	var json addRecordRequest
	if ok := utilsreq.BindBodyWithJson(ctx, log, &json); !ok {
		return
	}

	db := utilsreq.MustGetDB(ctx, log);
	if db == nil {
		return
	}

	if err := db.AddRecord(json.Text); err != nil {
		log.Error("Cannot write db", utilslog.SlogErrWrapper(err))
		utilsreq.InternalError(ctx)
		return
	}

	ctx.JSON(http.StatusOK, gin.H{})
}