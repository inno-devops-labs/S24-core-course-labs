package moscowTime

import io.vertx.core.Vertx
import sttp.tapir.{plainBody, query}
import sttp.tapir.ztapir._
import sttp.tapir.server.vertx.zio.VertxZioServerInterpreter
import sttp.tapir.server.vertx.zio.VertxZioServerInterpreter._
import zio._
import io.vertx.ext.web.Route

object Main extends ZIOAppDefault {
  override implicit val runtime = Runtime.default

  override def run: ZIO[Environment & (ZIOAppArgs & Scope), Any, Any] = (for {
    server <- ZIO.service[Server]
    _ <- server.run
  } yield ()).provide(
    Router.live,
    Server.live,
    MoscowDateTime.live
  )
}
