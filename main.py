#!/usr/bin/python
#FRANCIS E ESTER
import sys
sys.path.append("../..")

import grammar
import errors

imprimir=True
filename = "teste.txt"

arquive = open(filename).read()

grammar.parser.parse(arquive)

if imprimir:
    print(grammar.var_global)
