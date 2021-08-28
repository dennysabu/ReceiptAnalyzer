import json 
import sys

class FoodOrder:
     def __init__(self, item, quantity, price) -> None:
         self.item = item
         self.quantity = quantity,
         self.price = price

def get_mechant_info(result):
     merc = result['analyzeResult']['documentResults'][0]['fields']
     print(merc['MerchantAddress']['text'])


def get_items(result):
     items = result['analyzeResult']['documentResults'][0]['fields']['Items']['valueArray']
     ordered = []
     for item in items:
          food = item['valueObject']['Name']['text']
          quant = item['valueObject']['Quantity']['text']
          price = item['valueObject']['TotalPrice']['text']
          print(f'{food} - {quant} - {price}')

if __name__ == '__main__':
     print('Starting Analysis')
     f = open(sys.argv[1], 'r')
     data = json.loads(f.read())
     f.close()
     
     get_mechant_info(data)
     get_items(data)