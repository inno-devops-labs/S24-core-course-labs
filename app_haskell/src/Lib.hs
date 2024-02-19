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

server :: Server API
server = liftIO (iso8601Show <$> getCurrentMoscowTime)

app :: Application
app = serve (Proxy @API) server
