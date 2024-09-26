package moscowTime

import java.time.LocalDateTime
import zio.*
import java.time.{ZoneId, ZonedDateTime}

trait MoscowDateTime {
  def getCurrentTime: UIO[ZonedDateTime]
}

class MoscowDateTimeImpl extends MoscowDateTime {
  def getCurrentTime: UIO[ZonedDateTime] = Clock.currentDateTime
    .map(_.atZoneSameInstant(ZoneId.of("Europe/Moscow")))
}

object MoscowDateTime {
  def live = ZLayer.succeed(new MoscowDateTimeImpl)
}
