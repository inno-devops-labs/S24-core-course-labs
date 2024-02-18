package time.moscow

import com.softartdev.kronos.Network
import com.softartdev.kronos.sync
import io.ktor.server.application.Application
import kotlinx.datetime.Clock
import time.moscow.plugins.configureHTTP
import time.moscow.plugins.configureRouting

fun main(args: Array<String>) {
    io.ktor.server.netty.EngineMain.main(args)
}

fun Application.module() {
    Clock.Network.sync()
    configureHTTP()
    configureRouting()
}
