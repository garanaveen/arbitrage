#!/usr/bin/env python

class Asset:
   def __init__(self):
      self.currency = None
      self.holdings = 0

   def __init__(self, c, h):
      self.currency = c
      self.holdings = h

class ExchangeAssets:
   name = 'Exchange'
   
   def __init__(self):
      self.name = 'Exchange'
      self.assetList = [] #List of Asset

   def __init__(self, n):
      self.name = n
      self.assetList = [] #List of Asset
   
   def AddAsset(self, asset):
      self.assetList.append(asset)
   
   def PrintAssets(self):
      print ("Holdings on " + self.name + ",")
      for asset in self.assetList:
         print (asset.currency, asset.holdings)
   
class CurrentAssets:
   def __init__(self):
      self.assets = [] #List of ExchangeAssets
   
   def AddExchange(self, exchange):
      self.assets.append(exchange)

   def PrintAssets(self):
      for exchange in self.assets:
         exchange.PrintAssets()


if __name__ == "__main__":
   btconkoinex = Asset('BTC', 0.3)
   ltconkoinex = Asset('LTC', 3)
   assetsonkoinex = ExchangeAssets('koinex')
   assetsonkoinex.AddAsset(btconkoinex)
   assetsonkoinex.AddAsset(ltconkoinex)

   ethongdax = Asset('ETH', 2)
   bchongdax = Asset('BCH', 1)
   assetsongdax = ExchangeAssets('gdax')
   assetsongdax.AddAsset(ethongdax)
   assetsongdax.AddAsset(bchongdax)

   allmyassets = CurrentAssets()
   allmyassets.AddExchange(assetsonkoinex)
   allmyassets.AddExchange(assetsongdax)


   allmyassets.PrintAssets()


