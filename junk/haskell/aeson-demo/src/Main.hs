{-# LANGUAGE DeriveGeneric, RecordWildCards, OverloadedStrings #-}

module Main where

import Network.HTTP.Conduit (simpleHttp)
import qualified Data.ByteString.Lazy as BSL
import Data.Aeson
import Data.Text
import GHC.Generics
import Control.Monad
import Control.Applicative
import Data.Maybe

data Currency = Currency { 
  base :: Text,
  date :: Text,
  rates :: Object } deriving(Show, Generic)

instance FromJSON Currency where
  parseJSON = withObject "currency" $ \o -> do
    base <- o .: "base"
    date <- o .: "date"
    rates <- o .: "rates"
    return Currency{..}

jsonURL :: String
jsonURL = "https://api.fixer.io/latest"

getJSON :: IO BSL.ByteString
getJSON = simpleHttp jsonURL

main :: IO ()
main = do
  jsonOut <- (eitherDecode' <$> getJSON) :: IO (Either String Currency)
  case jsonOut of
    Right err -> print err
    Left ps -> print ps