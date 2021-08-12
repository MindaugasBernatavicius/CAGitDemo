import logging
from Calculator import Calculator
import yaml
import argparse

parser = argparse.ArgumentParser(description='Simple calculator')
help_str = 'method to call in the program (divide, add, multiply)'
parser.add_argument('--method', required=False, type=str, nargs='?', help=help_str)
args = parser.parse_args()

formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')

file_logger = logging.FileHandler('..\\logs\\main.log')
file_logger.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(file_logger)

with open('../config/main_config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)['app']

calc = Calculator()

res = 0
if args.method == None:
    if config['method_to_illustrate'] == 'divide':
        res = calc.divide(3, 0)
    elif config['method_to_illustrate'] == 'add':
        res = calc.add(3, 2)
    elif config['method_to_illustrate'] == 'multiply':
        res = calc.multiply(3, 2)
elif args.method == 'divide':
    res = calc.divide(3, 0)
elif args.method == 'add':
    res = calc.add(3, 2)
elif args.method == 'multiply':
    res = calc.multiply(3, 2)

method = config['method_to_illustrate'].upper() if args.method is None else args.method.upper()
logger.warning('{} : {}'.format(method + ' result', res))


print("This is added in branch add-more-logic!")
print("This is added in branch add-more-logic!!!++")
