import adafruit_dht
import time
import requests

# Thingspeak API URL and API key
URL = 'https://api.thingspeak.com/update?api_key=BNDT4518NSNNIYTG'


dht_device = adafruit_dht.DHT11(23)

MQ135_PIN = 2  


while True:
    try:
       
        temperature = dht_device.temperature
        humidity = dht_device.humidity

        #
        mq135_reading = 0  

        
        print(f"Humidity= {humidity:.2f}%")
        print(f"Temperature= {temperature:.2f}°C")
        print(f"CO2 Level= {mq135_reading}")

        
        params = {'field2': temperature, 'field3': humidity, 'field4': mq135_reading}

        
        response = requests.get(URL, params=params)

       
        print(response)

    except RuntimeError as error:
       
        print(error)


    time.sleep(15)
