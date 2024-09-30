#!/bin/python3

import math
import os
import random
import re
import sys


class Item():
  """Class that initializes an item."""
    def __init__(self, name, price):
      """Initializes the item's name and price variables"""
        self.name = name
        self.price = price

class ShoppingCart:
  """Class that manages a shopping cart by adding items and returning the total price."""
    def __init__(self):
      """Initializes the cart and total price variables."""
        self.cart = []
        self.price_total = 0
    
    def __len__(self):
      """Returns the number of items added in the cart.
      
      Returns
      -------
      len(self.cart): int
          The number of items in the cart.
      """
        return len(self.cart)
    
    def add(self, item: Item):
      """Adds an item to the shopping cart.

      Parameters
      ----------
      item: Item
          The item to be added to the cart.
      """
        self.cart.append(item.name)
        self.price_total += item.price
    
    def total(self):
      """Returns the shopping cart's total price.

      Returns
      -------
      self.price_total: float
          The shopping cart's total price.
      """
        return self.price_total
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()
