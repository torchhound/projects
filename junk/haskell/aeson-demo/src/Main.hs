{-# LANGUAGE DeriveGeneric, DeriveAnyClass #-}

module Main where

import Network.HTTP.Conduit (simpleHttp)
import qualified Data.ByteString.Lazy as BSL
import Data.Aeson
import Data.Text
import GHC.Generics
import Control.Monad
import Control.Applicative

data Currency = 
  Currency { base :: Text
           , date :: Text
           , rates :: Array
           } deriving(Show, Generic, FromJSON)

jsonURL :: String
jsonURL = "https://api.fixer.io/latest"

getJSON :: IO BSL.ByteString
getJSON = simpleHttp jsonURL

main :: IO ()
main = do
  jsonOut <- (fmap eitherDecode getJSON) :: IO (Either String [Currency])
  case jsonOut of
    Left err -> putStrLn err
    Right ps -> print ps
