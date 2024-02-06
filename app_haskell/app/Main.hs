module Main (main) where

import Network.Wai.Handler.Warp
import Lib (app)

main :: IO ()
main = do
  putStrLn "Listening on port 8081..."
  run 8081 app
