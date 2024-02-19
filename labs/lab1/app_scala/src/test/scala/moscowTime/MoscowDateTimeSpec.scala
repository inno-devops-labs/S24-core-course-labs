package moscowTime

import zio.test.*
import zio.ZIO
import scala.concurrent.duration.*
import zio.test.Assertion._
import zio.test.TestClock
import zio.Clock.ClockLive
import zio.ZLayer
import java.util.TimeZone
import java.time.ZoneId
import zio.Clock
import java.time.Instant

object MoscowDateTimeSpec extends ZIOSpecDefault {
  val deps = MoscowDateTime.live

  override def spec =
    suite("Moscow Time Spec")(
      test("should be different from current time in London") {
        for {
          _ <- TestClock.setTimeZone(ZoneId.of("Europe/London"))
          _ <- TestClock.setTime(Instant.now)
          currentDateTime <- Clock.currentDateTime
          moscowTime <- ZIO.service[MoscowDateTime]
          now <- moscowTime.getCurrentTime
        } yield assertTrue(
          now.toLocalDateTime != currentDateTime.toLocalDateTime
        )
      },
      test("be the same as current time in Moscow") {
        for {
          _ <- TestClock.setTimeZone(ZoneId.of("Europe/Moscow"))
          _ <- TestClock.setTime(Instant.now)
          currentDateTime <- Clock.currentDateTime
          moscowTime <- ZIO.service[MoscowDateTime]
          now <- moscowTime.getCurrentTime
        } yield assertTrue(
          now.toLocalDateTime == currentDateTime.toLocalDateTime
        )
      }
    ).provide(
      deps
    )
}
