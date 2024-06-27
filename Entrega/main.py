from ply.lex import lex
from ply.yacc import yacc
import os


# Analise Lexica

tokens = (
    'INICIO', 'MONITOR', 'EXECUTE', 'TERMINO', 'ENQUANTO', 'FACA', 'FIM', 
    'ID', 'NUMBER', 'EQUALS', 'ZERO', 'PLUS', 'MULTIPLY', 'COMMA', 'LPAREN', 'RPAREN',
    'IF', 'THEN', 'ELSE','EVAL', 'NEG', 'ENDIF'
)

reserved = {
    'INICIO': 'INICIO',
    'MONITOR': 'MONITOR',
    'EXECUTE': 'EXECUTE',
    'TERMINO': 'TERMINO',
    'ENQUANTO': 'ENQUANTO',
    'FACA': 'FACA',
    'FIM': 'FIM',
    'ZERO': 'ZERO',
    'IF': 'IF',
    'ENDIF': 'ENDIF',
    'THEN': 'THEN',
    'ELSE': 'ELSE',
    'EVAL': 'EVAL',
}

t_EQUALS = r'='
t_PLUS = r'\+'
t_NEG = r'\-'
t_MULTIPLY = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex()

# ########################################################################################


# Análise sintática

precedence = (
    ('left', 'PLUS', 'MULTIPLY'),
    ('right', 'NEG'),
)

vars_to_monitor = []

def p_programa(p):
    'programa : INICIO varlist MONITOR monitor EXECUTE cmds TERMINO'
    p[0] = f"#include <stdio.h>\n\nint main() {{\n{p[2]}\n{p[4]}\n{p[6]}\n\nreturn 0;\n}}"

def p_monitor(p):
    '''monitor : varlist
               '''
    p[0] = p[1]
    # Armazena as variáveis monitoradas
    global vars_to_monitor
    qtd_monitored_vars = len(p[1].split(';')) - 1
    vars_to_monitor = vars_to_monitor[-qtd_monitored_vars:]


def p_varlist(p):
    '''varlist : ID COMMA varlist
               | ID'''

    if len(p) == 4:
        p[0] = f"int {p[1]};\n{p[3]}"
    elif len(p) == 2:
        p[0] = f"int {p[1]};"
    
    global vars_to_monitor
    vars_to_monitor.append(p[1])


def p_cmds(p):
    '''cmds : cmd cmds
            | cmd'''
    if len(p) == 3:
        p[0] = f"{p[1]}\n{p[2]}"
    else:
        p[0] = p[1]


def p_cmd(p):
    # Versao nova
    '''cmd : ID EQUALS expr
           | ZERO LPAREN ID RPAREN
           | ENQUANTO ID FACA cmds FIM
           | IF expr THEN cmds ELSE cmds ENDIF
           | IF expr THEN cmds ENDIF
           | EVAL LPAREN expr COMMA expr COMMA cmds RPAREN
           | EVAL cmds NUMBER FIM'''


    global vars_to_monitor
    if p[2] == '=':
        p[0] = f"{p[1]} = {p[3]};"
        if(p[1] in vars_to_monitor):
            p[0] += f"\nprintf(\"\'{p[0]}\' => Z = %d\\n\", {p[1]});" # Adiciona o printf para monitorar a variável

    elif p[1] == 'ZERO':
        p[0] = f"{p[3]} = 0;"
        if(p[3] in vars_to_monitor):
            p[0] += f"\nprintf(\"\'{p[0]}\' => Z = %d\\n\", {p[3]});" # Adiciona o printf para monitorar a variável
        
    elif p[1] == 'ENQUANTO':
        p[0] = f"while ({p[2]} != 0) {{\n{p[4]}\n}}"
    elif p[1] == 'IF':
        if len(p) == 8:
            p[0] = f"if ({p[2]}) {{\n{p[4]}\n}} else {{\n{p[6]}\n}}"
        else:
            p[0] = f"if ({p[2]}) {{\n{p[4]}\n}}"
    elif p[1] == 'EVAL' and len(p) == 9:
        p[0] = f"for (int i = {p[3]}; i > {p[5]}; --i) {{\n{p[7]}\n}}"
    elif p[1] == 'EVAL' and len(p) == 5:
        p[0] = f"for (int i = 0; i < {p[3]}; ++i) {{\n{p[2]}\n}}"

def p_expr(p):
    '''expr : expr PLUS expr
            | expr MULTIPLY expr
            | LPAREN expr RPAREN
            | NUMBER
            | ID
            | NEG expr %prec NEG'''
    if len(p) == 4 and p[1] != '(':
        if p[2] == '+':
            p[0] = f"{p[1]} + {p[3]}"
        elif p[2] == '*':
            p[0] = f"{p[1]} * {p[3]}"
    elif len(p) == 4:
        p[0] = p[2]
    elif len(p) == 5:
        p[0] = f"{p[3]} = 0"
    elif len(p) == 3:
        p[0] = f"-{p[2]}"
    else:
        p[0] = p[1]

def p_error(p):
    print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")

parser = yacc()


# ########################################################################################


def provolone_to_c(arquivo_entrada, arquivo_saida):
    if not os.path.isfile(arquivo_entrada):
        print(f"Arquivo de entrada '{arquivo_entrada}' não encontrado.")
        return
    
    with open(arquivo_entrada, 'r') as f:
        codigo_provol_one = f.read()
    
    # Limpa a lista de variáveis monitoradas
    global vars_to_monitor
    vars_to_monitor = []

    result = parser.parse(codigo_provol_one)
    
    if result:
        with open(arquivo_saida, 'w') as f:
            f.write(result)
        print(f"Código traduzido com sucesso para '{arquivo_saida}'")
    else:
        print("Falha na tradução. Verifique o código de entrada.")


for file in os.listdir("./inputs"):
    print(file)
    if file.endswith(".txt"):
        arquivo_entrada = f"./inputs/{file}"
        arquivo_saida = f"./outputs/{file.replace('.txt', '.c')}"

        print(f"Traduzindo {file}...")
        provolone_to_c(arquivo_entrada, arquivo_saida)
        print()
