from math import factorial
from math import sqrt
from math import log
import linecache
import sys, traceback
from string import replace
from webwork_parser import parse_webwork, WebworkParseException, node_string
import traceback
import operator as op
from scipy.stats import norm

#import logging 
#logger=logging.getLogger('evaluate')

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    #logger.error('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def ncr(n, r):
    " compute n choose r "
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    ans = numer/denom
    try:
        float(ans)
    except OverflowError:
        raise Exception('C(%s, %s) is too large and cause over flow'%(n,r))
    return ans

def npr(n, r):
    " Computer n permute r (order matters)"
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    try:
        float(numer)
    except OverflowError:
        raise Exception('P(%s, %s) is too large and cause over flow'%(n,r))
    return numer

def find_common_values(e1,e2):
    """ Find intersection of values in two eval trees.
        If a value is found, all of the values in the subtree below it are ignored.

    returns: common,only_in_1, only_in_2
       Dicts of the form {value: (from,to) } where value is a float.
       
    """
    
def eval_parsed(e, variable_list={}, label='R'):
    """ Evaluate a parsed expression, returns a tree, of the same form as the parse tree. Where each operator 
        is replaced by a tuple: (operator,evaluation result)

        variable_list = {variable_name: number used to test}
    
        Still need to write code to handle varibles, lists and sets.
    """
    #print 'in eval_parsed e=|%s|, label=|%s|'%(str(e),str(label))

    def get_number(ev):
        if not ev:
            #logger.error('Eval_parsed: None object from get_number')
            return
        if len(ev)==4 and ev[0]=='X': 
            return float(ev[1])
        elif len(ev)==1:
            return float(ev[0])
        else: 
            return float(ev[0][1])
        
    try:
        #logger.debug('Eval_parsed: e="'+str(e)+'"')
        if type(e)==type(None):
            return 0
        elif is_number(e)==1:
            return (float(e),)
        elif len(e)==2:
            [[f,span],op]=e

            if f=='{}':
                return [[f,None,span,label],op]  # if element is a list, just return as is.
            elif f=='V':
                if op=='e':
                    ans = 2.71828183
                    return ['X',ans,span,label]
                elif variable_list:
                    ans = variable_list[op]
                    return ['X',ans,span,label]
                else:
                    raise Exception("%s doesn't have a value for evaluation"%op)

            ev=eval_parsed(op, variable_list, label=label+'.0')
            if not ev:
                return
                
            v=get_number(ev)
            
            if f=='X':  # X indicates a single number
                ans=v
                return [f,ans,span,label]
            elif f=='-':
                ans=-v
            elif f=='!':
                if v < 1000:
                    ans=factorial(v)
                else:
                    raise Exception('%s is too large to apply factorial'%v)
            elif f=='Q':
                ans= 1-norm.cdf(v)
            elif f=='Phi':
                ans = norm.cdf(v)
            elif f=='sqrt':
                ans = sqrt(v)
            elif f=='log':
                ans = log(v)
            else:
                raise Exception('unrecognized unary operator %s in %s'%(f,e))
            return [[f,ans,span,label],ev]
        
        elif len(e)==3:
            [[f,span],op1,op2]=e
            ev1=eval_parsed(op1, variable_list, label=label+'.0')
            ev2=eval_parsed(op2, variable_list, label=label+'.1')

            if not ev1 or not ev2:
                return
            v1=get_number(ev1)
            v2=get_number(ev2)

            if f=='+':    ans= v1+v2
            elif f=='*':  ans= v1*v2
            elif f=='-':  ans= v1-v2
            elif f=='/':  ans= v1/v2
            elif f=='**': ans= v1**v2
            elif f=='^': ans= v1**v2
            elif f=='C':
                ans= ncr(int(v1), int(v2))
            elif f=='P':
                ans= npr(int(v1), int(v2))
            else:
                raise Exception('unrecognized binary operator %s in %s'%(f,e))
            return_value=[[f,ans,span,label],ev1,ev2]
            #print 'returned value=',return_value
            return return_value
        else:
            raise Exception('Unrecognized expression form: %s'%e)
    except Exception as ex:
        #print 'Eval_parsed Exception:',ex
        #traceback.print_exc()
        #traceback.print_exc(file=sys.stdout)
        return None
        #raise WebworkParseException(ex)
        # return ((e[0][0], None, e[0][1]),)


def Collect_numbers(etree):
    T={}
    if type(etree)==int:
        return T
    collection_recursion(T,etree)
    return T

def collection_recursion(T,etree):
    if len(etree)==1:
        T[etree[0]]=etree   # add leaf
    if len(etree)>1:
        T[etree[0][1]]=etree   # add evaluation for non-leaf
        for i in range(1,len(etree)):
            collection_recursion(T,etree[i])

def numbers_and_exps(etree, string):
    numbers = Collect_numbers(etree)
    ret = {k: node_string(v, string) for k, v in numbers.iteritems()}
    return ret

def parse_and_collect_numbers(string):
    try:
        parse_tree, variables = parse_webwork(string)
        if len(variables)==0:
            eval_tree = eval_parsed(parse_tree)
            eval_numbers = Collect_numbers(eval_tree)
            return set(eval_numbers.keys())
        else: 
            return Eval_with_Variables(string,variables)
    except:
        return set()

def substitute(expression,variables,values):
    """ Substitutes values for variables in an expression
        expression: a string holding the expression
        variables: (returned as a secnd value by parse_webwork)
                   a list of tuples. Each tuple consists of two values:
                    - The name of the variable (as a string)
                    - The locations where the variable appears
        values: A dictionary that relates a numerical value to each variable
    """
    if set(values.keys()) != set(variables.keys()):
        raise Exception('substitute: there should be a exactly one value for each variable'+
                        'variables='+str(variables),
                        'values='+str(values));
    #merge the location lists and put them in order
    loc_list=[]
    for name,locs in variables.items():
        for L in locs:
            loc_list.append((name,L))
    loc_list=sorted(loc_list,key=lambda x:x[1])
    
    loc=0
    sub_expression=''   # hold the buffer that will become the substituted expression
    for var_name,new_loc in loc_list:
        value=values[var_name]
        if expression[new_loc:new_loc+len(var_name)] == var_name:
            sub_expression+=expression[loc:new_loc]+str(value)
            loc = new_loc+len(var_name)
        else:
            raise Exception(('Error in variable locations, expression=%s'+\
                             ' variable name=%s, locations=%s')%\
                              (expression,var_name,str(var_loc)))
    sub_expression+=expression[loc:]
    return sub_expression
            
def parse_and_eval(string,values=[]):
    expr,variables = parse_webwork(string)
    try:
        if expr:
            if len(variables)==0:
                etree = eval_parsed(expr)
                return etree,{}
            if len(variables)!=len(values):
                return expr,variables # if the number of values does
                                      # not match number of variables,
                                      # return the description of the
                                      # variables.
            else:
                                      # if number of values matches
                                      # number of variables then
                                      # substitute values for
                                      # variables and call parser
                                      # again on numerical expression.
                subs_string=substitute(string,variables,values)
                subs_expr,variables=parse_webwork(subs_string)
                assert len(variables)==0;
                if subs_expr:
                    etree=eval_parsed(subs_expr)
                    return etree,{}
                        
        else:
            raise Exception
    except:
        #logger.error('Eval_parsed: Exception in parse_and_eval, string=%s, parsed=%s'%(string,str(expr)))
        traceback.print_exc(file=sys.stdout)
        return None

if __name__=="__main__":
    string=sys.argv[1]
    print 'input:::',string
    tree,variables=parse_webwork(string)
    print 'output:::',tree, variables
    eval_tree=eval_parsed(tree)
    print 'Eval_tree:::',eval_tree
