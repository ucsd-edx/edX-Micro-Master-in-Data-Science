import ply.lex as lex
import webwork_parser
# from webwork_parser import WebworkParseException

class WebworkLexer(object):
    tokens = (
        'Q', 'PHI', 'CHOOSE', 'SQRT', 'LOG', 'PERMUTE', 'VARIABLE', 'NUMBER', 'PLUS','MINUS','TIMES','DIVIDE', 'LPAREN','RPAREN','FACTORIAL', \
        'LSET', 'RSET','COMMA','EXP', 'LBRACKET', 'RBRACKET','COMPUTE'
    )

    # Tokens
    t_Q         = r'Q'
    t_PHI       = r'Phi'
    t_SQRT      = r'sqrt'
    t_LOG       = r'log'
    t_CHOOSE    = r'C'
    t_PERMUTE   = r'P'
    t_PLUS      = r'\+'
    t_MINUS     = r'-'
    t_FACTORIAL = r'!'
    t_TIMES     = r'\*'
    t_DIVIDE    = r'/'
    t_EXP       = r'\^|(\*\*)'
    t_LPAREN    = r'\('
    t_RPAREN    = r'\)'
    t_LBRACKET  = r'\['
    t_RBRACKET  = r'\]'
    t_LSET      = r'\{'
    t_RSET      = r'\}'
    #t_QUOTE     = r"'"
    #t_DBL_QUOTE = r'"'
    t_COMPUTE   = r'Compute'
    t_COMMA     = r'\,'
    # switching from PERL variables, used to randomize the problem, to actual variables, assumed to be single characters.
    t_VARIABLE  = r'(?<![A-Za-z])[ABD-OR-Za-z](?![A-Za-z])'

    def t_NUMBER(self, t):
        r'\d*\.?\d+(E(\+|\-)?\d+)?'
        #print 'entered webwork_lexer.t_Number(%s)'%t.value
        try:
            t.value = int(t.value)
            #print 'parsed as int'
        except ValueError:
            try:
                t.value = float(t.value)
                #print 'parsed as float'
            except ValueError:
                print t
                raise webwork_parser.WebworkParseException("LEXER: Trouble parsing float %s", t.value)
        return t

    # Ignored characters
    t_ignore = " \t\'\""
    
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        raise webwork_parser.WebworkParseException(
            "LEXER: Illegal character '%s' at location %1d" % \
            (t.value[0], t.lexpos))

    def __init__(self,**kwargs):
        # Build the lexer
        self.lexer = lex.lex(module=self, **kwargs)
    
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok: break
             print tok

    def example1(self):
        string = '(C(52,5) - 4*C(32,5))/(5!)'
        self.test(string)
    
    @classmethod
    def selftest(klass):
        l = klass()
        l.example1()

