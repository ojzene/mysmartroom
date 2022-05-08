import serial
import urllib.request

URL = "https://api.thingspeak.com/update"

# copy the API KEY from your ThingSpeak channel
APIKEY = "3TU9D7NGYHW7WDIZ"

# copy the port from your Arduino editor
PORT = 'COM4'

ser = serial.Serial(PORT, 9600)

def upload(data):
  args = {'api_key' : APIKEY }
  for i in range(len(data)):
    args["field"+str(i+1)] = float(data[i])
  query_data = urllib.parse.urlencode(args).encode('utf-8')
  headers = {"Content-type": "application/x-www-form-urlencoded",
             "Accept": "text/plain"}
  req = urllib.request.Request(URL,query_data,headers)
  response = urllib.request.urlopen(req)
  return response

while True:
    message = ser.readline()
    print(message.strip().decode())
    upload(message.split())