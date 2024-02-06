package time.moscow

import com.softartdev.kronos.Network
import com.softartdev.kronos.sync
import io.ktor.server.application.*
import time.moscow.plugins.*
import kotlinx.datetime.Clock

fun main(args: Array<String>) {

    io.ktor.server.netty.EngineMain.main(args)
}

fun Application.module() {
    Clock.Network.sync()
    configureHTTP()
    configureRouting()
}
