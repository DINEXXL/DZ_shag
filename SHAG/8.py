# import logging
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='logs.log',
#     filemode='w',
#     format='%(asctime)s: %(levelname)s - %(massage)s'
# )
#
# try:
#     print(10 / 0)
# except Exception as e:
#     logging.exception('Zero division')
#     # print(e)

# if 2 + 2 == 4:
#     print('Yes')
#
# assert 2 + 2 == 5, 'it is wrong'

# """
# >>> 2 + 2
# 5
#
# >>> 3 * 8
# 123
# """
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

def adder(*args, **kwargs):
    res = 0
    for _ in args:
        res += _
    for _ in kwargs.values()
        res += _
        
    return res