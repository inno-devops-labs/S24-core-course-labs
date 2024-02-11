package time.moscow.plugins

import com.softartdev.kronos.Network
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.html.*
import io.ktor.server.routing.*
import kotlinx.datetime.Clock
import kotlinx.datetime.TimeZone
import kotlinx.datetime.toLocalDateTime
import kotlinx.html.*


fun Application.configureRouting() {
    routing {
        get("/") {

            val time = Clock.Network.now().toLocalDateTime(TimeZone.of("Europe/Moscow"))
            call.respondHtml(HttpStatusCode.OK) {
                head {
                    title {
                        +"Moscow Time"
                    }
                }
                body {
                    h1 {
                        +"Hello, Moscow!"
                    }
                    p {
                        +String.format(
                            "(%s) %s %d %d %02d:%02d:%02d",
                            time.dayOfWeek.name,
                            time.month.name,
                            time.dayOfMonth,
                            time.year,
                            time.hour,
                            time.minute,
                            time.second)
                    }
                }
            }
        }
    }
}
