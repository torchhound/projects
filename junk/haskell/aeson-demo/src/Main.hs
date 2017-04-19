{-# LANGUAGE DeriveGeneric #-}

module Main where

import Network.HTTP.Conduit (simpleHttp)
import qualified Data.ByteString.Lazy as BSL

jsonURL :: String
jsonURL = "https://api.fixer.io/latest"

getJSON :: IO BSL.ByteString
getJSON = simpleHttp jsonURL

main :: IO ()
main = do
  jsonOut <- getJSON
  BSL.putStr jsonOut
