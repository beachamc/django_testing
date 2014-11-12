#!/usr/bin/python

import sys
sys.path.append('./')
sys.path.append('../')
import django
from django.core.paginator import *

def main():
    args = sys.argv[1:]

    inputs = args[2].split(',')
    myBool = eval(inputs[0])
    n = inputs[1]
    paginator = eval(args[0])

    try:
        eval('paginator.'+args[1])
    except Exception as e:
        if(type(e) == PageNotAnInteger):
            print "PageNotAnInteger"
        elif(type(e) == EmptyPage):
            print "EmptyPage"
        else:
            print type(e)
    else:
        print eval('paginator.'+args[1])

if __name__ == '__main__':
    main()