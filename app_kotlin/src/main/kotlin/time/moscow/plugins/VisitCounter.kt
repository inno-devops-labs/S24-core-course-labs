package time.moscow.plugins

import io.ktor.server.application.createApplicationPlugin
import java.io.File
import time.moscow.filePath


val VisitCounterPlugin = createApplicationPlugin(name = "VisitCounter") {
    onCall { call ->
        val file = File(filePath)
        if (!file.exists()) {
            file.writeText("0")
        }
        val visits = file.readText().trim().toInt()
        file.writeText((visits + 1).toString())
    }
}