package moscowTime

import io.vertx.core.Vertx
import io.vertx.ext.web.{Router => VRouter}
import sttp.tapir.{plainBody, query}
import sttp.tapir.ztapir._
import sttp.tapir.files.staticFileGetServerEndpoint
import sttp.tapir.server.vertx.zio.VertxZioServerInterpreter
import sttp.tapir.server.vertx.zio.VertxZioServerInterpreter._
import zio._
import io.vertx.ext.web.Route
import sttp.tapir.ztapir._
import zio.*
import io.vertx.ext.web.Route
import sttp.capabilities.zio.ZioStreams
import java.time.format.DateTimeFormatter

trait Router {
  def route: VRouter => Route
}

class RouterImpl(moscowDateTime: MoscowDateTime) extends Router {
  given Runtime[Any] = zio.Runtime.default

  val styleEndpoint: ZServerEndpoint[Any, ZioStreams] =
    resourceGetServerEndpoint("style.css")(getClass.getClassLoader, "style.css")

  val moscowDateTimeEndpoint =
    endpoint
      .out(header("Content-Type", "text/html"))
      .out(plainBody[String])

  def moscowDateTimeLogic = moscowDateTime.getCurrentTime.map { dateTime =>
    val dateFormatted =
      dateTime.toLocalDate.format(DateTimeFormatter.ofPattern("MMMM dd, yyyy"))
    val timeFormatted =
      dateTime.toLocalTime.format(DateTimeFormatter.ofPattern("HH:mm:ss"))
    f"""
          |<!doctype html>
          |<html lang="en">
          |  <head>
          |    <meta charset="UTF-8" />
          |    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          |    <link
          |      rel="stylesheet"
          |      href="style.css"
          |    />
          |  </head>
          |  <body>
          |    <div class="date-time">
          |      <p id="date">${dateFormatted}</p>
          |      <p id="time">${timeFormatted} MSK</p>
          |    </div>
          |  </body>
          |</html>
          |""".stripMargin
  }

  val endpointsWithLogic = List(
    styleEndpoint,
    moscowDateTimeEndpoint.zServerLogic[Any](_ => moscowDateTimeLogic)
  )

  override def route: VRouter => Route = { router =>
    endpointsWithLogic.foreach { endpoint =>
      VertxZioServerInterpreter().route(endpoint).apply(router)
    }
    router.route()
  }
}

object Router {
  def live: ZLayer[MoscowDateTime, Nothing, Router] = ZLayer.fromZIO {
    for {
      moscowDateTime <- ZIO.service[MoscowDateTime]
    } yield new RouterImpl(moscowDateTime)
  }

}
