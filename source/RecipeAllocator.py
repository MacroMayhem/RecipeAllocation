import json
import os
from source.Order import  Order
from source.StockItem import StockItem
from source.GreedyAllocationAlgorithm import  GreedyAllocationAlgorithm
import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class RecipeAllocator:
    def __init__(self,orders_data=None, stock_data=None):
        self.__stocks = None
        self.__orders = None
        self.__load_stock(stock_data)
        self.__load_orders(orders_data)


    @property
    def stocks(self):
        return self.__stocks

    @property
    def orders(self):
        return self.__orders


    def __load_stock(self, json_data):
        self.__stocks = []
        for recipe, stock_count in json_data.items():
            try:
                self.__stocks.append(StockItem(name=recipe, portions=stock_count['stock_count']))
            except Exception as e:
                logger.error(e)
                continue



    def __load_orders(self, json_data):
        self.__orders = []
        for number_of_recipes, order_portions in json_data.items():
            for portion_name, portion_number in order_portions.items():
                try:
                    self.__orders.append(Order(number_of_recipes=number_of_recipes, number_of_portions=portion_name,
                                           order_count=portion_number))
                except Exception as e:
                    logger.error(e)
                    continue

    def compute(self):
        algorithm = GreedyAllocationAlgorithm(orders=self.orders,stocks=self.stocks)
        return algorithm.output()

