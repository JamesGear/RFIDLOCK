# RFIDLOCK
Jako závěrečný projekt jsem si vybral zámek na dveře, který bude mít odemykání pomocí RFID karty/klíčenky.Chtěl bych zkusit práci s ESP8266. Chip bude komunikovat s MQTT a Mosquitto.

Základní princip : 
Uživatel přiloží klíčenku k zámku, zámek přečte kód uložený na klíčence, kód se přes WIFI zašle na MQTT server, pokud se k bude shodovat s kódem v databázi, pošle zpátky signál pro otevření dveří, pokud ne, pošle signál pro bzučák, který vydá zvuk jako zamítnutí.

Známe problémy :
využití flask-bones,
virtual box na kterém měl běžet MQTT server nefunguje zároveň s Dockerem který je potřeba pro flask-bonek

reference :
https://www.instructables.com/id/TfCD-NFC-Beer-Lockbox/
https://www.makeuseof.com/tag/diy-smart-lock-arduino-rfid/
https://3dprint.com/53583/nfc-door-lock-qduino-mini/
https://bbs.espressif.com/viewtopic.php?t=133
https://github.com/petrgru/karty (školní chipy)
https://www.root.cz/clanky/protokol-mqtt-komunikacni-standard-pro-iot/
https://iotta.cz/esp8266-mqtt/
http://www.steves-internet-guide.com/into-mqtt-python-client/
https://test.mosquitto.org/
            
potřebné díly : 
https://www.umakov.cz/elektricky-zamek-250x28mm-12v/d-69501-c-2662/
RFID čtečka ✓
ESP8266 ✓
nepájivé pole ✓
kabely ✓
bzučák ✓
RFID chipy a karty ✓
 
