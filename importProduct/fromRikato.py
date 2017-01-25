import json
from pprint import pprint



with open('goods_residues.json') as data_file:
    data = json.load(data_file)

# f = open("test.txt", 'w')
# pprint(data, stream=f, indent=4)

#TODO
"""
1. сравнить категории, и добавить недостающие

2. сравнить товары, и добавить недостающие, так-же сравнить цены закупки,
и при необходимости их поменять

3. сравнить и добавить цену с носорога(при добавлении, или изменении закупочной цены)

4. добавить категории

5. добавить продукты
"""
