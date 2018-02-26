#!/bin/bash
CURRENCY=BTC
wget https://koinex.in/api/ticker -O koinexprice.txt -o /dev/null
wget https://api.gdax.com/products/BTC-USD/ticker -O gdaxbtc.txt -o /dev/null
wget https://api.gdax.com/products/LTC-USD/ticker -O gdaxltc.txt -o /dev/null
wget https://api.fixer.io/latest?base=USD -O usdinr.txt -o /dev/null
koinex=$(cat koinexprice.txt | jq -r '.prices.BTC')
koinexltc=$(cat koinexprice.txt | jq -r '.prices.LTC')
gdax=$(cat gdaxbtc.txt |jq -r '.price')
gdaxltc=$(cat gdaxltc.txt |jq -r '.price')
conversionrate=$(cat usdinr.txt | jq -r '.rates.INR')
koinexinusd=$(bc -l <<< "scale=2; $koinex/$conversionrate")
koinexltcinusd=$(bc -l <<< "scale=2; $koinexltc/$conversionrate")
difference=$(bc -l <<< "scale=2; $gdax-$koinexinusd")
differenceltc=$(bc -l <<< "scale=2; $gdaxltc-$koinexltcinusd")
ratio=$(bc -l <<< "scale=2; $difference*100/$gdax")
ratioltc=$(bc -l <<< "scale=2; $differenceltc*100/$gdaxltc")

echo "Gdax : $gdax"
echo "Koinex : $koinex"
echo "Koinexinusd : $koinexinusd"
echo "Ratio : $ratio%"
#echo "Koinex : $koinex"
echo "If ratio is positive then sell on gdax and buy on koinex"
currentdate=$(date "+%Y-%m-%d-%H:%M:%S")
echo "currentdate: $currentdate"
echo "$currentdate, gdax:$gdax, koinex:$koinexinusd, btcratio:$ratio" >> history_arbitrage.txt
echo "$currentdate, gdaxltc:$gdaxltc, koinexltc:$koinexltcinusd, ltcratio:$ratioltc" >> history_arbitrage.txt
tail -n 2 history_arbitrage.txt
