
"""

try:
    <code with possible error>
except <Error or tuple of errors>:
    <code executed is case of error>
else:                   - optional
    <code executed in case of no errors>
finally:                - oprtional
    <code executed whether is an error>

except NameError:
except (ValueError, NameError):


try:
    <code with possible error>
except NameError:
    <code executed is case of error>
except ValueError:
    <code executed is case of error>
"""

try:
    print(10 / 0)
except ZeroDivisionError:
    print('we have an error')

try:
    print(10 / 2)
except ZeroDivisionError:
    print('we have an error')
else:
    print('We have no errors')
finally:
    print('Code that exactly runs')

print('=======')

try:
    print(10 / 0)
except ZeroDivisionError:
    print('we have an error')
else:
    print('We have no errors')
finally:
    print('Code that exactly runs')

def checker(value):
    if not isinstance(value, str):
        raise TypeError(
            f'Sorry, we cant work with {type(value)}, we need str.'
        )
    else:
        print(value)

x = '10'
checker(x)

class BuildError(Exception):

    def __str__(self):
        return 'Not enough lot of materials. We cannot build the house'

def check_materials(value, limit=300):
    if value . limit:
        return 'enough materials'
    else:
        raise BuildError

our_materials = 30
check_materials(our_materials)

import warnings

warnings.simplefilter('ignore', SyntaxWarning)
warnings.simplefilter('ignore', ImportWarning)

warnings.warn('NO code here', SyntaxWarning)
try:
    warnings.warn('NO module here', ImportWarning)
except:
    print('Error was processed')

warnings.warn('NO module here', ImportWarning)