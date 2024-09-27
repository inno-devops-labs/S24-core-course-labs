ThisBuild / scalaVersion := "3.3.1"
ThisBuild / version := "1.0.0"

lazy val root = (project in file("."))
  .settings(
    name := "moscowTime",
    libraryDependencies ++= Dependencies.allDependencies,
    testFrameworks += new TestFramework("zio.test.sbt.ZTestFramework")
  )

assembly / assemblyJarName := "moscowTime.jar"

assembly / assemblyMergeStrategy  := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case "module-info.class"            => MergeStrategy.first
  case "META-INF/io.netty.versions.properties" => MergeStrategy.first
  case x =>
    val oldStrategy = (assembly / assemblyMergeStrategy).value
    oldStrategy(x)
}
