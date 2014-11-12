#!/usr/bin/python

import sys
sys.path.append('./')
sys.path.append('../')
from django.core.paginator import *

def main():
    args = sys.argv[1:]

    n = int(args[2])

    constructor = args[0].split()

    paginator = eval(constructor[0])
    page = eval(constructor[1])

    try:
        eval('page.'+args[1])
    except Exception as e:
        print type(e)
    else:
        print eval('page.'+args[1])

if __name__ == '__main__':
    main()