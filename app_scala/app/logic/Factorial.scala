package logic

import play.api.libs.json.JsError
import play.api.libs.json.JsResult.Exception

import scala.annotation.tailrec

case class Factorial(n: Int) {
  @tailrec
  private def calculate(n: Int, acc: Long): Long = n match {
    case 1          => acc
    case n if n > 1 => calculate(n - 1, acc * n)
    case _          => throw Exception(JsError("n can not be negative"))
  }

  def get: Long = calculate(n, 1)
}
