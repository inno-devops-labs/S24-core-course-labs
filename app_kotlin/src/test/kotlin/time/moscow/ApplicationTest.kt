package time.moscow

import io.ktor.client.call.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import io.ktor.http.*
import io.ktor.server.testing.*
import kotlin.test.*
import time.moscow.plugins.*
import java.lang.Thread.sleep

class ApplicationTest {

    @Test
    fun requestTest() = testApplication {
        application {
            configureRouting()
        }

        client.get("/").apply {
            assertEquals(HttpStatusCode.OK, status)
        }
    }

    @Test
    fun notEqualContentTest() = testApplication {
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
