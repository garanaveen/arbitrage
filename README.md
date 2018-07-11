# arbitrage

This is a python script to calculate the price diffence for coins between gdax and koinex exchange.
You can set alerts to send an email when the price diffence crosses the limits you set in myalerts.ini


How to use the script,

clone the repo and run being inside arbitrage directory
cp emailcredentialstemplate.py emailcredentials.py (update the contents in emailcredentials.py only if you want email notification. emailcredentials.py is in .gitignore, so it isn't a part of repo and is supposed to reside just in your local directory. Preferably create a new gmail account just for this purpose.)
Run ./arbitrage


----------------------------------------------------------------
Python packages that are needed for running the python script,
wget -  ( probably needs to be installed using pip installer for python)

Numbers are logged in to history_arbitrage.log

Nothing is stored in database. Currently everything is logged in to history_arbitrage.log

Install list,
python (as in python2)
sudo apt install sqlite

-----------------
First install pip3,
sudo apt-get install python3-pip
Then install pyqt5 using pip3
pip3 install pyqt5
-----------------

