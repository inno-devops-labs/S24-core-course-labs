module Main where

import Lib (moscowTimeZone, getCurrentMoscowTime)
import Control.Concurrent (threadDelay)
import Data.Time.Calendar.OrdinalDate
import Data.Time.LocalTime (ZonedTime(..), LocalTime(..), diffLocalTime)
import System.Exit (exitFailure, exitSuccess)

type Test = IO Bool

test :: String -> IO Bool -> Test
test name t = do
  putStr (name ++ "... ")
  passed <- t
  putStrLn (if passed then "passed" else "failed")
  return passed

testCurrentTimeIsInMoscowTimeZone :: Test
testCurrentTimeIsInMoscowTimeZone = test "Moscow timezone" $ do
  time <- getCurrentMoscowTime
  let zone = zonedTimeZone time
  return (zone == moscowTimeZone)

testCurrentTimeIsNotTooOld :: Test
testCurrentTimeIsNotTooOld = test "Current time is not old" $ do
  ZonedTime { zonedTimeToLocalTime = LocalTime { localDay = YearDay year day } } <-
    getCurrentMoscowTime
  return (year >= 2024 && day >= (31 + 19))

testCurrentTimeIsMonotonic :: Test
testCurrentTimeIsMonotonic = test "Current time is monotonic" $ do
  ZonedTime { zonedTimeToLocalTime = time1 } <- getCurrentMoscowTime
  threadDelay (100 * 1000) -- 0.1 s
  ZonedTime { zonedTimeToLocalTime = time2 } <- getCurrentMoscowTime

  let diff = time2 `diffLocalTime` time1
  return (time2 >= time1 && diff >= 0.1 && diff <= 0.2)

tests :: [Test]
tests =
  [ testCurrentTimeIsInMoscowTimeZone
  , testCurrentTimeIsNotTooOld
  , testCurrentTimeIsMonotonic
  ]

main :: IO ()
main = do
  allPassed <- and <$> sequence tests
  if allPassed
    then do
      putStrLn "All tests passed"
      exitSuccess
    else do
      putStrLn "Some tests failed"
      exitFailure
