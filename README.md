RFID zámek 

Jako závěrečný projekt jsem si vybral systém zámků na dveře s odemykáním pomocí RFID chipu/karty, pro práci jsem si zvolil mikrokontroler ESP8266. Rozhodl jsem po domluvě s p. učitelem Grussmannem pro využití technologií: MQTT; Mosquitto; Flask bones; Docker 

 

Základní princip: 

Uživatel přiloží RFID kartu ke čtečce u dveří, po přiložení se ESP probudí a odešle přes wifi požadavek na server ve kterém se ověří jestli je uživatel registrovaný, patří do skupiny firmy a má-li časový přístup, pokud vše ověří a výsledek je kladný, pošle se zpátky signál, který otevře dveře. 

 

Reference: 

https://www.instructables.com/id/TfCD-NFC-Beer-Lockbox/ zámek dveří na NFC 

https://www.makeuseof.com/tag/diy-smart-lock-arduino-rfid/ zámek dveří na RFID 

https://3dprint.com/53583/nfc-door-lock-qduino-mini/ zámek dveří při využití arduina 

https://bbs.espressif.com/viewtopic.php?t=133 https://github.com/petrgru/karty RFID chipy fungující na škole 

https://www.root.cz/clanky/protokol-mqtt-komunikacni-standard-pro-iot/ základní zprovoznění MQTT protokolu 

https://iotta.cz/esp8266-mqtt/ propojení ESP a MQTT 

http://www.steves-internet-guide.com/into-mqtt-python-client/ nastavení MQTT pro python 

https://test.mosquitto.org/ veřejný Mosquitto server 

 

Potřebné díly: 

Elektrický zámek dveří 

RFID čtečka 

ESP8266 

Pole na pájení 

Kabely 

Bzučák 

RFID chip/karta 

 

 

 

 

 

 

Instalace Flask Bones 

    Nainstalujeme Docker pro windows (https://hub.docker.com/editions/community/docker-ce-desktop-windows) 

    Docker musí být nastavený na “Linux constainers” 

    Sdílení disků musí být povoleno 
    ![Docker Shared Files](https://github.com/JamesGear/RFIDLOCK/blob/master/DockerSharedDrives.PNG)

    Poté stáhneme a nainstalujeme PostrgreSQL (https://www.postgresql.org/download/) 

     

 

 

 

 

 

 

 

 

 
