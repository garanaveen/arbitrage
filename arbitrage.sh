#!/bin/bash
wget https://koinex.in/api/ticker -O koinexprice.txt -o /dev/null
wget https://api.gdax.com/products/BTC-USD/ticker -O gdax.txt -o /dev/null
wget https://api.fixer.io/latest?base=USD -O usdinr.txt -o /dev/null
koinex=$(cat koinexprice.txt | jq -r '.prices' |jq -r '.BTC')
gdax=$(cat gdax.txt |jq -r '.price')
conversionrate=$(cat usdinr.txt | jq -r '.rates' |jq -r '.INR')
koinexinusd=$(bc -l <<< "scale=2; $koinex/$conversionrate")
difference=$(bc -l <<< "scale=2; $gdax-$koinexinusd")
ratio=$(bc -l <<< "scale=2; $difference*100/$gdax")

echo "Gdax : $gdax"
echo "Koinexinusd : $koinexinusd"
echo "Ratio : $ratio%"
#echo "Koinex : $koinex"
echo "If ratio is positive then sell on gdax and buy on koinex"
currentdate=$(date "+%Y-%m-%d-%H:%M:%S")
echo "currentdate: $currentdate"
echo "$currentdate, gdax:$gdax, koinex:$koinexinusd, ratio:$ratio" >> history_arbitrage.txt
tail -n 1 history_arbitrage.txt
