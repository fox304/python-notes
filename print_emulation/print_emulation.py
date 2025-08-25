import sys


def print3(*args, **kargs):
    '''
    эмуляция печати
    '''
    sep = kargs.get('sep', ' ')
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print3(1, 2, 3, sep='??', end='.\n', file=sys.stderr)