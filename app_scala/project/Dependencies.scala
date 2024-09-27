import sbt._

object Dependencies {
  object V {
    val zio = "2.0.21"
    val tapir = "1.9.9"
    val missingLink = "0.2.11"
  }

  lazy val zio = Seq("dev.zio" %% "zio" % V.zio)

  lazy val zioTest = Seq(
    "dev.zio" %% "zio-test" % V.zio,
    "dev.zio" %% "zio-test-sbt" % V.zio,
    "dev.zio" %% "zio-test-magnolia" % V.zio
  )

  lazy val tapir = Seq(
    "com.softwaremill.sttp.tapir" %% "tapir-core" % V.tapir,
    "com.softwaremill.sttp.tapir" %% "tapir-files" % V.tapir,
    "com.softwaremill.sttp.tapir" %% "tapir-vertx-server-zio" % V.tapir
  )

  lazy val missingLink = Seq("com.spotify" % "missinglink-core" % V.missingLink)

  // Fixing missing links
  lazy val missingLinkFix = Seq(
    "ch.qos.logback" % "logback-classic" % "1.4.14",
    "com.aayushatharva.brotli4j" % "brotli4j" % "1.16.0",
    "com.fasterxml.jackson.core" % "jackson-databind" % "2.12.5",
    "com.github.luben" % "zstd-jni" % "1.5.0-2",
    "com.jcraft" % "jzlib" % "1.1.3",
    "io.netty" % "netty-all" % "4.1.106.Final",
    "io.netty" % "netty-tcnative" % "2.0.62.Final",
    "log4j" % "log4j" % "1.2.17",
    "org.apache.logging.log4j" % "log4j-api" % "2.14.1",
    "org.bouncycastle" % "bcpkix-jdk15on" % "1.68",
    "org.conscrypt" % "conscrypt-openjdk" % "2.2.1",
    "org.eclipse.jetty.alpn" % "alpn-api" % "1.1.2.v20150522" % "provided",
    "org.eclipse.jetty.npn" % "npn-api" % "1.1.1.v20141010" % "provided",
    "org.slf4j" % "slf4j-api" % "1.7.32"
  )

  val allDependencies = zio ++ zioTest ++ tapir ++ missingLink ++ missingLinkFix
}
