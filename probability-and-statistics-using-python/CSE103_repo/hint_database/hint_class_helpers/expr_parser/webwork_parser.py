import sys,os
import pickle
import copy
from traceback import print_exc
import ply.lex as lex
import ply.yacc as yacc
from math import factorial
from webwork_lexer import WebworkLexer

# Set up a logging object
# import logging

# logging.basicConfig(
#     level = logging.WARNING,
#     level = logging.INFO,
#     format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
# logger=logging.getLogger(__name__)

"""
Parsing webwork expressions
written by Matt Elkherj, Yoav Freund

The main method is:

parse_webwork - returns a tree, represented as nested listss.
Where expression is a string containing what should be a valid webwork answer (otherwise an exception is thrown).
Example: parse_webwork('C(32,5) - C(20,5)')
Answer: (('-', (0, 16)), (('C', (0, 6)), 32, 5), (('C', (10, 16)), 20, 5))
"""

associative_ops = ['*','+']

def node_span(node):
    if type(node)==list and type(node[0])==list:
        if len(node[0]) == 2: # Parse tree
            return node[0][1]
        elif len(node[0]) == 3: # Evaluation tree
            return node[0][2]

def node_string(node, string):
    if len(node) > 1:
        span = node_span(node)
        return string[span[0]:[span[1]+1]]
    else:
        return str(node[0])

def reduce_associative(tree):
    ''' Given a tree of nested operations, group nested associative operations into a single list.
        For example:

        >> reduce_associative(  ('*',('*',1,2),3)  )
#        ('*', 1, 2, 3)
        '''
    if type(tree) == list:
        #reduce subtrees
        subtrees = list(map(reduce_associative, tree[1:]))
        op = tree[0]
        if op in associative_ops:
            subtrees2 = [op]
            for t in subtrees:
                if (type(t) == list) and (t[0] == op):
                    subtrees2 += list(t[1:])
                else:
                    subtrees2.append(t)
            return list(subtrees2)
        else:
            return list([op]+subtrees)
    else:
        return tree

def flatten_list(L):
    """ Flatten a hierarchical list into one level """
    if not isinstance(L, list):
        #print 'flatten_list, non-list',L
        return [L]
    elif len(L)==1:
        #print 'flatten_list, len 1 list',L
        return flatten_list(L[0])
    # This line seems to error sometimes, seems like L or L[0] can be an int somehow
    elif L[0][0]!='list':
        #print 'flatten_list, header is not "list"',L
        return [L]
    else:
        #print 'flatten_list, real list ',L
        items=[]
        for i in range(1,len(L)):
            items=items+flatten_list(L[i])
        #print 'returning',items
        return items

def tree_to_s_exp(tree):
    '''Convert an expression parse tree to a lisp-style s-expression'''
    if type(tree) == list or type(tree) == list:
        return '('+tree[0][0] + ' ' + ' '.join(tree_to_s_exp(child) for child in tree[1:]) +')'
    else:
        return str(tree)

class WebworkParseException(Exception):
    pass

def handle_comma_separated_number(expr):
    ''' Handles numbers of the form 1,234,562.09842 or 1,234,562 returning the
         numeric value
         returns None if the expression is not of this form '''
    expr_without_commas = ''.join( (c for c in expr if c != ',') )
    if len(expr) == len(expr_without_commas):
        return None
    else:
        try:
            return int(expr_without_commas)
        except (TypeError, ValueError):
            try:
                return float(expr_without_commas)
            except (TypeError, ValueError):
                return None

# Parsing rules
precedence = (
    ('nonassoc','VARIABLE'),
    ('left','LIST'),
    ('nonassoc','COMMA'),
    ('left','IMPL_TIMES'),
    ('nonassoc','UMINUS'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('left','EXP'),
    ('left','FACTORIAL'),
    ('nonassoc','CHOOSE'),
    ('nonassoc','PERMUTE'),
    ('nonassoc','Q'),
    ('nonassoc','PHI'),
    ('nonassoc','SQRT'),
    ('nonassoc','LOG'),
    ('nonassoc','COMPUTE')
)

def p_statement_expr_list(p):
    '''statement : expression
                 | factor
                 | list
                 '''
    p[0] = p[1]

def add_header(t): # append the span of the expression to the header
    #print '-'*50+'add_header got:',type(t)
    i=0
    #for x in t:
    #    print i,str(x), t.lexspan(i)
    #    i+=1
    return [[t[0][0],list(t.lexspan(0))],]+t[0][1:]

def p_expression_ops(t):
    '''expression : expression PLUS factor  %prec PLUS
                  | factor PLUS factor      %prec PLUS
                  | expression MINUS factor %prec PLUS
                  | factor MINUS factor     %prec PLUS
                  '''
    if t[2] == '+'  : t[0] = ['+',t[1],t[3]]
    elif t[2] == '-': t[0] = ['-',t[1],t[3]]
    t[0]=add_header(t)

def p_factor_ops(t):
    '''factor : factor TIMES factor    %prec TIMES
                | factor DIVIDE factor %prec DIVIDE
                | factor EXP factor    %prec EXP
                  '''
    if t[2] == '*': t[0] = ['*',t[1],t[3]]
    elif t[2] == '/': t[0] = ['/', t[1], t[3]]
    elif t[2] == '^' or t[2] == '**': t[0] = ['^',t[1],t[3]]
    t[0]=add_header(t)

def p_expression_implicit_times(t):
    '''factor : factor factor %prec IMPL_TIMES'''
    t[0] = ['*',t[1],t[2]]
    t[0]=add_header(t)

def p_expression_uminus(t):
    'factor : MINUS factor %prec UMINUS'
    t[0] = ['-',t[2]]
    t[0]=add_header(t)

def p_expression_factorial(t):
    'factor : factor FACTORIAL %prec FACTORIAL'
    t[0] = ['!',t[1]]
    t[0]=add_header(t)

def p_expression_choose(t):
    'factor : CHOOSE LPAREN list RPAREN %prec CHOOSE'
    list=flatten_list(t[3][1:])
    t[0] = ['C',list[0],list[1]]
    t[0]=add_header(t)

def p_expression_permute(t):
    'factor : PERMUTE LPAREN list RPAREN %prec PERMUTE'
    list=flatten_list(t[3][1:])
    t[0] = ['P',list[0],list[1]]
    t[0]=add_header(t)

def p_factor_q(t):
    '''factor : Q LPAREN factor RPAREN %prec Q
              | Q LPAREN expression RPAREN %prec Q'''
    t[0] = ['Q', t[3]]
    t[0]=add_header(t)

def p_factor_phi(t):
    '''factor : PHI LPAREN factor RPAREN %prec PHI
              | PHI LPAREN expression RPAREN %prec PHI'''
    t[0] = ['Phi', t[3]]
    t[0]=add_header(t)

def p_expression_group(t):
    '''factor : LPAREN expression RPAREN
              | LBRACKET expression RBRACKET
              | LPAREN factor RPAREN
              | LBRACKET factor RBRACKET
              '''
    t[0] = t[2]

def p_factor_sqrt(t):
    '''factor : SQRT LPAREN factor RPAREN %prec SQRT
              | SQRT LPAREN expression RPAREN %prec SQRT'''
    t[0] = ['sqrt', t[3]]
    t[0]=add_header(t)

def p_factor_log(t):
    '''factor : LOG LPAREN factor RPAREN %prec LOG
              | LOG LPAREN expression RPAREN %prec LOG'''
    t[0] = ['log', t[3]]
    t[0]=add_header(t)

def p_compute(t):
    '''factor : COMPUTE LPAREN expression RPAREN
              | COMPUTE LPAREN factor RPAREN
              '''
    t[0] = t[3]


def p_expression_unbalanced_group(t):
    '''factor : LPAREN expression
              | LBRACKET expression
              | LPAREN factor
              | LBRACKET factor
              '''
    print "Parse Error: Unbalanced Group Operator"
    print t.lexer.lexdata
    print ' '*(t.lexpos(0))+'^'
    raise WebworkParseException('Unbalanced grouping operator in expression: ' + t.lexer.lexdata)

def p_expression_unclosed_choose(t):
    'factor : CHOOSE LPAREN list'
    print "Parse Error: Unclosed Choose"
    print t.lexer.lexdata
    print ' '*(t.lexpos(0))+'^'
    raise WebworkParseException('Unbalanced parentheses in expression: ' + t.lexer.lexdata)

def p_expression_unclosed_permute(t):
    'factor : PERMUTE LPAREN list'
    print "Parse Error: Unclosed PERMUTE"
    print t.lexer.lexdata
    print ' '*(t.lexpos(0))+'^'
    raise WebworkParseException('Unbalanced parentheses in expression: ' + t.lexer.lexdata)

def p_expression_set(t):
    '''factor : LSET list RSET
                | LSET expression RSET
                | LSET RSET '''
    if len(t) == 4:
        List=flatten_list(t[2][1:])
        t[0] = ['{}',list(List)]
    else:
        t[0] = ('{}',[])
    t[0]=add_header(t)

def p_expression_list(t):
    'factor : LPAREN list RPAREN'
    t[0] = ['()',t[2]]
    t[0]=add_header(t)


def p_nonempty_list(t):
    ''' list  : expression COMMA
              | list expression COMMA
              | list expression
              | factor COMMA
              | list factor COMMA
              | list factor %prec LIST '''
    #print 'nonempty_list:',len(t),
    #for i in range(len(t)):
    #    print 't[%1d]='%i, t[i],';',
    #print

    if len(t) == 3 and t[2] == ',':                #eg 1,
        t[0] = ['list',[t[1],]]
    elif len(t) == 4 or len(t) == 3:               #eg ...1, or ...1
        t[0] = ['list',t[1] + [t[2],]]
    t[0]=add_header(t)

def p_factor_number(t):
    '''factor  : NUMBER'''
    pos=t.lexpos(0)
    # print 'p_expression_number',t[1],pos

    t[0]=[['X',[pos,pos+len(str(t[1]))-1]],t[1]]

def p_factor_variable(t):
    '''factor   : VARIABLE %prec VARIABLE'''
    pos=t.lexpos(0)
    var=t[1];
    global variables
    if var in variables.keys():
        variables[var].append(pos)
    else:
        variables[var]=[pos]
    
    t[0]=[['V',[pos,pos+len(str(t[1]))-1]],t[1]]


def p_error(p):
    if p is None:
        raise WebworkParseException('yacc:Syntax error - Empty token')
    else:
        #start,end = p.lexpos
        raise WebworkParseException("yacc:Syntax error at '%s',location=%1d" % (p,p.lexpos))

# def p_error(p):
#     if p==None:
#         print "Syntax error at end of expression"
#     else:
#         print "Syntax error at <<", p,p.lexspan(0),'>>'
#     # Just discard the token and tell the parser it's okay.
#     yacc.token()

# START lex and yacc
lexer = WebworkLexer(debug=False)
tokens = lexer.tokens
parser = yacc.yacc(debug=False)

# set up debugging.

#lex.lex(debug=True,debuglog=log,errorlog=log)
#yacc.yacc(debug=True,debuglog=log,errorlog=log)

def parse_webwork(expr):
    """parse input expression string
    @output: parse tree and variables"""
    global variables
    variables={} # a list that stores the locations in which each variable appears.
    parsed = handle_comma_separated_number(expr)
    if parsed is None: #didn't match comma_separated_number, so parse expr
        try:
            parsed = parser.parse(expr,tracking=True, lexer=lexer.lexer)
            final_range=fix_ranges(parsed)
            #logger.debug('final_range='+str(final_range))
            #print 'final_range='+str(final_range)
        except WebworkParseException as e:
            #logger.error('||%s|| %s', expr, e)
            #logger.exception(e)
            print "Error in parser {0}, {1}".format(expr, e)
            parsed=None
        except UnicodeEncodeError as e:
            print "Error in parser. Unicode Encode Exception: {0}".format(e)
        except Exception as e:
            #logger.error('||%s|| %s', expr, e)
            #logger.exception(e)
            print "Error in parser {0}, {1}".format(expr, e)
            parsed = None
    return parsed,variables

def fix_ranges(p):
    """the goal of this function s to fix a bug(?) in ply.yacc which is
    that the lexspan() function returns ranges which the last index
    corresponds to the beginning of the last literal. This causes problems when parsing expressions such as 
    '200/300' in which case the span of the whoe expression is (0,4) and does not contain the last two digits in 300
    """
    #print 'entered fix_ranges with input  '+str(p),type(p)
    try:
        if p[0][0] in ['X','V']:  # found a leaf: a number or a variable name
            pass
        elif type(p[0][0])==str and type(p[0][1])==list and type(p[0][1][0])==int and type(p[0][1][1])==int:
            #print 'fix_ranges found a list whose head is operator,range'
            mx=[p[0][1][0],p[0][1][1]]
            for item in p[1:]:
                #print 'about to process',item,mx
                span=fix_ranges(item)
                #print 'span of item = ',span, 'mx=',mx
                mx[0]=min(mx[0],span[0])
                mx[1]=max(mx[1],span[1])
                #print 'in loop mx=',str(mx),'span=',str(span)

            if mx[0]<p[0][1][0] or mx[1]>p[0][1][1]:
                # print 'found error in spans, tree=',str(p),'old=',p[0][1],'new=',mx
                p[0][1]=mx
        else:
            #logger.error('fix_ranges failed to recognize list'+str(p))
            print 'fix_ranges failed to recognize list'+str(p)
    except:
        print_exc()

    return p[0][1]

#if __name__ == '__main__':
#    webwork = pickle.load(open(os.path.join(sys.argv[1],'pickled_data'),'rb'))
#    exprs = [expr for _,_,expr in webwork.all_attempts]
#    parse_webwork(exprs[0])

if __name__ == '__main__':
    string=sys.argv[1]
    print 'input:::',string
    tree=parse_webwork(string)
    print 'output:::',tree
