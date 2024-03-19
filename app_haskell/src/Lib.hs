{-# LANGUAGE DataKinds #-}
{-# LANGUAGE TypeApplications #-}

module Lib (getCurrentMoscowTime, moscowTimeZone, app) where

import Data.Time.Clock (getCurrentTime)
import Data.Time.LocalTime
  (ZonedTime, TimeZone, hoursToTimeZone, utcToZonedTime)
import Data.Time.Format.ISO8601 (iso8601Show)
import Control.Monad.IO.Class (liftIO)
import Servant

moscowTimeZone :: TimeZone
moscowTimeZone = hoursToTimeZone 3

getCurrentMoscowTime :: IO ZonedTime
getCurrentMoscowTime = utcToZonedTime moscowTimeZone <$> getCurrentTime

type API = Get '[PlainText] String

handleRequest :: IO String
handleRequest = do
  putStrLn "Handling a request"
  iso8601Show <$> getCurrentMoscowTime

server :: Server API
server = liftIO handleRequest

app :: Application
app = serve (Proxy @API) server
