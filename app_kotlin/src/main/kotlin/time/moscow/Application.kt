package time.moscow

import com.softartdev.kronos.Network
import com.softartdev.kronos.sync
import io.ktor.server.application.Application
import io.ktor.server.application.install
import kotlinx.datetime.Clock
import time.moscow.plugins.VisitCounterPlugin
import time.moscow.plugins.configureHTTP
import time.moscow.plugins.configureRouting

fun main(args: Array<String>) {
    io.ktor.server.netty.EngineMain.main(args)
}

var filePath = "visits.txt"

fun Application.module() {
    filePath = environment.config.propertyOrNull("ktor.persistent.filePath")?.getString() ?: "visits.txt"
    Clock.Network.sync()
    install(VisitCounterPlugin)
    configureHTTP()
    configureRouting()
}
