package moscowTime

import io.vertx.core.Vertx
import io.vertx.ext.web.Route
import io.vertx.ext.web.{Router => VRouter}
import sttp.tapir.{plainBody, query}
import sttp.tapir.ztapir._
import sttp.tapir.server.vertx.zio.VertxZioServerInterpreter
import sttp.tapir.server.vertx.zio.VertxZioServerInterpreter._
import zio._

trait Server {
  def run: UIO[Unit]
}

class ServerImpl(router: Router) extends Server {
  override def run: UIO[Unit] = {
    ZIO.scoped(
      ZIO
        .acquireRelease(
          ZIO
            .attempt {
              val vertx = Vertx.vertx()
              val server = vertx.createHttpServer()
              val vertxRouter = VRouter.router(vertx)
              router.route(vertxRouter)
              server.requestHandler(vertxRouter).listen(8080)
            }
            .flatMap(_.asRIO)
        ) { server =>
          ZIO.attempt(server.close()).flatMap(_.asRIO).orDie
        } *> ZIO.never
    )
  }.catchAll(e => ZIO.logError(s"Error: $e"))
}

object Server {
  def live: ZLayer[Router, Nothing, Server] = ZLayer.fromZIO {
    for {
      router <- ZIO.service[Router]
    } yield new ServerImpl(router)
  }
}
