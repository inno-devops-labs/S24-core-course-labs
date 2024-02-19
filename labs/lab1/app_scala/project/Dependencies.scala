import sbt._

object Dependencies {
  object V {
    val zio = "2.0.21"
    val tapir = "1.9.9"
  }

  lazy val zio = "dev.zio" %% "zio" % V.zio

  lazy val zioTest = "dev.zio" %% "zio-test" % V.zio
  lazy val zioTestSbt = "dev.zio" %% "zio-test-sbt" % V.zio
  lazy val zioTestMagnolia = "dev.zio" %% "zio-test-magnolia" % V.zio

  lazy val tapir = "com.softwaremill.sttp.tapir" %% "tapir-core" % V.tapir
  lazy val tapirFiles = "com.softwaremill.sttp.tapir" %% "tapir-files" % V.tapir
  lazy val tapirVertx =
    "com.softwaremill.sttp.tapir" %% "tapir-vertx-server-zio" % V.tapir

  val allDependencies =
    Seq(zio, zioTest, zioTestSbt, zioTestMagnolia, tapir, tapirFiles, tapirVertx)

}
