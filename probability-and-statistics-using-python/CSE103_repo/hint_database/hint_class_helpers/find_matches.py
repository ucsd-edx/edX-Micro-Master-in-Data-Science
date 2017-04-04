from expr_parser import webwork_parser
from expr_parser import Eval_parsed
from collections import deque
from collections import defaultdict

def flatten(tree,tag):
    """flatten a tree
    tag 'c' if it's answer
    tag 't' if it's attempt
    return a flatten sorted list"""
    List=[]
    Queue=deque([tree])
    try:
        while Queue:
            current=Queue.popleft()
            if type(current)==list: 
                if isinstance(current[0],basestring):
                    List.append([current[1],tag,current])
                elif isinstance(current[0][0],basestring) and isinstance(current[0][1],(int, long, float, complex)) and type(current[0][2])==list:
                    List.append([current[0][1],tag,current])
                    Queue.extend(current[1:])
                else:
                    return []
            else:
                return []
    except Exception as error:
        print 'error: current=', str(current)
        return []
    List=sorted(List,key=lambda x: x[0])
    return List


def get_top_node(tree):
    """return the starting index and ending index
        used to determine dominating hits"""
    if tree[2][0]=='X':
        return tree[2][3]
    elif type(tree[2][0])==list:
        return tree[2][0][3]
    else:
        print 'Error in get_top_node'
        return None



def find_Hits(List,tol = 1+1e-5):
    """ Given a combined list of subtrees from both attempt and answer,
    sorted by value, find the matching pairs of trees
    tol is the tolerance used to define which pairs of values match. 
    Needed because different expressions get different roundoff error
    """
    Hits=[]
    for i in xrange(0,len(List)-1):
        item1 = List[i]
        item2 = List[i+1]
        if item2[0] != 0:
            ratio=item1[0]/item2[0]
        else:
            if item1[0] == 0:
                ratio = 1
            else:
                ratio = 0
        # get the tree node
        node1 = get_top_node(item1)
        node2 = get_top_node(item2)
        if item1[1]!=item2[1] and ratio < tol and ratio > (1/tol) and node1 == node2:
            if item1[1]=='c':
                Hits.append((item1,item2))
            elif item2[1]=='c':
                Hits.append((item2,item1))
            else:
                print "Error in find_Hits. Neither item labeled c"
    return Hits


def get_span(tree):
    """return the starting index and ending index
        used to determine dominating hits"""
    if tree[2][0]=='X':
        return tree[2][2]
    elif type(tree[2][0])==list:
        return tree[2][0][2]
    else:
        print 'Error in get_span'
        return None


def find_dominating_hits(Hits,answer,attempt):
    """eliminate dominated hits from input Hits"""
    for i in range(len(Hits)):
        for j in range(len(Hits)):
            if i==j:
                continue
            span1=get_span(Hits[i][0])
            span2=get_span(Hits[j][0])
            # If it is dominated by other hits, marked as 'dc'
            if span1[0]<=span2[0] and span1[1]>=span2[1]:
                Hits[j][0][1]='dc'
    
    final_matches=[]
    for hit in Hits:
        # Do not include hits marked as 'dc'
        if hit[0][1]=='c':
            value=hit[0][0]
            span_c=get_span(hit[0])
            span_a=get_span(hit[1])
            answer_part=answer[span_c[0]:span_c[1]+1]
            attempt_part = attempt[span_a[0]:span_a[1]+1]
            if hit[0][2][0]=='X':
                node=hit[0][2][3]
            else:
                node=hit[0][2][0][3]
            final_matches.append((node,value,answer_part,attempt_part))
    return final_matches



def find_matches(params):
    """ return a list of hits """
    attempt=params['attempt']
    attempt_tree=params['att_tree']
    attempt_list=flatten(attempt_tree,'t')
    
    answer=params['answer']
    answer_tree=params['ans_tree']
    answer_list=flatten(answer_tree,'c')

    # sort by value
    combined_list=sorted(answer_list+attempt_list,key=lambda x: (x[0],len(x[2])))

    # find all hits
    Hits=find_Hits(combined_list)

    # eliminate dominating hits
    final_matches=find_dominating_hits(Hits,answer,attempt)
    
    return final_matches

