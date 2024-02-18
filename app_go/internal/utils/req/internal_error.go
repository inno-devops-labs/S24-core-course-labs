package utilsreq

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func InternalError(ctx *gin.Context) {
	ctx.JSON(http.StatusInternalServerError, gin.H{"error": "Internal Error"})
}