import json
from pprint import pprint



with open('goods_residues.json') as data_file:
    data = json.load(data_file)

# f = open("test.txt", 'w')
# pprint(data, stream=f, indent=4)

#TODO
#сравнить категории, и добавить недостающие

"""
сравнить товары, и добавить недостающие, так-же сравнить цены закупки,
и при необходимости их поменять
"""

#сравнить и добавить цену с носорога(при добавлении, или изменении закупочной цены)

#добавить категории

#add Product
