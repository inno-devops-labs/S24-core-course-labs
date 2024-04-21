{-# LANGUAGE DataKinds #-}
{-# LANGUAGE TypeApplications #-}
{-# LANGUAGE TypeOperators #-}

module Lib (getCurrentMoscowTime, moscowTimeZone, app) where

import Data.Time.Clock (getCurrentTime)
import Data.Time.LocalTime
  (ZonedTime, TimeZone, hoursToTimeZone, utcToZonedTime)
import Data.Time.Format.ISO8601 (iso8601Show)
import Control.Monad.IO.Class (liftIO)
import Servant
import Text.Read (readMaybe)
import Control.Exception (try)
import Data.Either (fromRight)

moscowTimeZone :: TimeZone
moscowTimeZone = hoursToTimeZone 3

visitsFile :: FilePath
visitsFile = "./data/visits"

getVisits :: IO Int
getVisits = do
  rawCounter <- fromRight "" <$> try @IOError (readFile visitsFile)
  case readMaybe rawCounter of
    Just counter -> return counter
    Nothing -> return 0

incrementVisits :: IO ()
incrementVisits = do
  counter <- getVisits
  writeFile visitsFile $ show (counter + 1)

getCurrentMoscowTime :: IO ZonedTime
getCurrentMoscowTime = utcToZonedTime moscowTimeZone <$> getCurrentTime

type API = Get '[PlainText] String :<|> "visits" :> Get '[PlainText] String

handleRequest :: IO String
handleRequest = do
  putStrLn "Handling a request"
  incrementVisits
  iso8601Show <$> getCurrentMoscowTime

handleVisits :: IO String
handleVisits = show <$> getVisits

server :: Server API
server = liftIO handleRequest :<|> liftIO handleVisits

app :: Application
app = serve (Proxy @API) server
