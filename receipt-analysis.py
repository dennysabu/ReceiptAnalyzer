import requests
import sys 
import json 
import time
import os

REQUEST_URL = os.environ['REQUEST_URL']
KEY = os.environ['REQUEST_KEY'] 


def make_request(file_path):

     f = None

     try:
          f = open(file_path, 'rb')
     except:
          pass

     if f is None:
          print('Fatal Error: Unable to open file.')
          sys.exit(-1)

     headers = {
          'Ocp-Apim-Subscription-Key': KEY,
          'Content-Type': 'image/png'
     }

     data = f.read()



     r = requests.post(REQUEST_URL, headers=headers, data=data)
     if r.status_code != 202:
          return None
     else: 
          return r.headers['Operation-Location']


def make_results_request(result_url):


     headers = {
          'Ocp-Apim-Subscription-Key': KEY,
     }


     r = requests.get(result_url, headers=headers)
     if r.status_code != 200:
          return None
     else: 
          return r.text




if __name__ == '__main__':
     print('Running OCR')
     result = make_request(sys.argv[1])
     if result is None:
          print('Unable to get result')
          sys.exit(-2)
     
     actual_result = make_results_request(result)
     if actual_result is None:
          print('Unable to get real result')
          sys.exit(-3)
     
     loaded = json.loads(actual_result)
     print('Loading Result...')

     while loaded['status'] == 'running':             # Processing can take a while and results might not be loaded
          time.sleep(5)                               # Not in a hurry for results, docs ask for 1s between requests. 
          actual_result = make_results_request(result)
          loaded = json.loads(actual_result)
          print('Waiting...')
     
     print('Results Loaded')
     with open('azure-results.json', 'w') as out:
          out.write(json.dumps(loaded, indent=2))
          out.flush()
          out.close()
     