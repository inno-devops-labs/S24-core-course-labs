// import Dependencies

ThisBuild / scalaVersion := "3.3.1"
ThisBuild / version := "1.0.0"

lazy val root = (project in file("."))
  .settings(
    name := "moscowTime",
    libraryDependencies ++= Dependencies.allDependencies,
    testFrameworks += new TestFramework("zio.test.sbt.ZTestFramework")
  )
