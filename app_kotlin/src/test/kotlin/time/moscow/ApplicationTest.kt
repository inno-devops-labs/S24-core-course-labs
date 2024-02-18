package time.moscow

import io.ktor.client.request.get
import io.ktor.client.statement.bodyAsText
import io.ktor.http.HttpStatusCode
import io.ktor.server.testing.testApplication
import time.moscow.plugins.configureRouting
import java.lang.Thread.sleep
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertNotEquals

class ApplicationTest {
    @Test
    fun requestTest() =
        testApplication {
            application {
                configureRouting()
            }

            client.get("/").apply {
                assertEquals(HttpStatusCode.OK, status)
            }
        }

    @Test
    fun notEqualContentTest() =
        testApplication {
            application {
                configureRouting()
            }
            val firstReq = client.get("/")
            sleep(3000)
            val secondReq = client.get("/")

            apply {
                assertEquals(HttpStatusCode.OK, firstReq.status)
                assertEquals(HttpStatusCode.OK, secondReq.status)

                assertNotEquals(firstReq.bodyAsText(), secondReq.bodyAsText(), "Responses before and after 3 seconds are the same")
            }
        }
}
