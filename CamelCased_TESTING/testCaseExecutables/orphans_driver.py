#!/usr/bin/python

import sys
sys.path.append('./')
sys.path.append('../')
from django.core.paginator import *

def main():
    args = sys.argv[1:]

    inputs = args[2].split(',')
    input = int(inputs[0])
    n = int(inputs[1])

    constructors = args[0].split()
    paginator = eval(constructors[0])
    page = eval(constructors[1])

    try:
        eval('page.'+args[1])
    except Exception as e:
        if(type(e) == PageNotAnInteger):
            print "PageNotAnInteger"
        elif(type(e) == EmptyPage):
            print "EmptyPage"
    else:
        print eval('page.'+args[1])

if __name__ == '__main__':
    main()