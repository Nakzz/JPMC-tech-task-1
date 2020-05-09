import unittest
from client import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2 ))

    print("test_getDataPoint_calculatePrice() done")


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2 ))
  
    print("test_getDataPoint_calculatePriceBidGreaterThanAsk() done")

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_checkDecimal(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2 ))
  
    print("test_getDataPoint_checkDecimal() done")


  def test_getDataPoint_checkNull(self):
    quotes = [
      {'top_ask': {'price': None, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': None, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': None, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': None, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
        self.assertEqual(getDataPoint(quote),(quote['stock'], 0, 0, 0 ))
  
    print("test_getDataPoint_checkNull() done")


  def test_getRatio_checkDecimal(self):
    prices = [
      [100,2.5],
      [100,3],
      [100,0.99]
    ]

    for price in prices:
      self.assertEqual(getRatio(price[0], price[1]), float(price[0])/price[1] )
    
    print("test_getRatio_checkDecimal() done")


  def test_getRatio_zeroDivision(self):
    prices = [
      [100,0],
      [100,0.0],
    ]

    for price in prices:
      self.assertEqual(getRatio(price[0], price[1]), None )
  
    print("test_getRatio_zeroDivision() done")


  def test_getRatio_checkNull(self):
    prices = [
      [100,None],
      [100,None],
    ]

    for price in prices:
      self.assertEqual(getRatio(price[0], price[1]), None )
  
    print("test_getRatio_checkNull() done")

if __name__ == '__main__':
    unittest.main()
