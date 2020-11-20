#!/usr/bin/python
import sys
sys.path.append("../..")

from ply import *

if "main" not in sys.argv[0]:
    print ("usage : main inputfile")
    raise SystemExit


'''
palavras reservadas
bool break for false if int return string true void while
'''
reserved = {
	'char'	:	'CHAR',
	'for'	:	'FOR',
	'if'	:	'IF',
	'else'	:	'ELSE',
	'int'	:	'INT',
	'float':	'FLOAT',
	'while'	:	'WHILE',
    'break' : 'BREAK',
    'switch':'SWITCH',
    'case':'CASE',
    'default':'DEFAULT'

}




tokens = ['NAME', 'NUMBER', 'NORMALSTRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
 'RPAREN', 'LPAREN', 'RCOLC', 'LCOLC', 'RBRACE', 'LBRACE', 'COMMA', 'SEMICOLON', 'OR', 'AND', 'EXPLAMATION', 'INTERROGATION', 'COLON',
 'EQUALS', 'DIFF', 'MENOR', 'MAIOR', 'MENOREQUALS', 'MAIOREQUALS', 'SUMEQUALS', 'MINUSEQUALS', 'TIMESEQUALS', 'DIVIDEEQUALS', 'MOD'
 ]+ list(reserved.values())


'''
tokens e simbolos
( ) [ ] { } , ; + - * / == != > >= < <= || && ! = += -= *= /= %= ? :
'''
t_ignore 		= ' \t'

t_RPAREN		= r'\)'
t_LPAREN		= r'\('


t_RCOLC			= r'\]'
t_LCOLC			= r'\['
t_RBRACE		= r'\}'
t_LBRACE		= r'\{'

t_COMMA			= r','
t_SEMICOLON		= r';'
t_OR 			= r'\|\|'
t_AND			= r'&&'
t_EXPLAMATION	= r'!'
t_INTERROGATION = r'\?'
t_COLON 		= r':'


t_EQUALS		= r'=='
t_DIFF			= r'!='
t_MENOR			= r'<'
t_MAIOR			= r'>'
t_MENOREQUALS	= r'<='
t_MAIOREQUALS 	= r'>='

t_SUMEQUALS		= r'\+='
t_MINUSEQUALS	= r'-='
t_TIMESEQUALS 	= r'\*='
t_DIVIDEEQUALS	= r'/='
t_MOD			= r'%='

t_PLUS   		= r'\+'
t_MINUS			= r'-'
t_TIMES			= r'\*'
t_DIVIDE		= r'/'
t_ASSIGN		= r'='

#t_ASPAS			= r'\"'

'''
t_CHAR 		= r'char'
t_FLOAT	    = r'float'
t_FOR		= r'for'
t_IF		= r'if'
t_INT		= r'int'
t_WHILE		= r'while'
t_PROCEDURE	= r'proc'
t_FUNCTION	= r'func'
'''



def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:# Check for reserved words
        t.type = reserved[ t.value ]
#	print(t)
    return t


def t_NORMALSTRING(t):
	r'\"([^\\\n]|(\\.))*?\"'
#	print(t)
	return t

def t_NUMBER(t):
	r'\d+'
#	print(t)
	t.value = int(t.value)
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT_MONOLINE(t):
    r'//.*'
    pass
    # No return value. Token discarded

def t_ccode_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

if __name__ == '__main__':
     lex.runmain()


lex.lex()
