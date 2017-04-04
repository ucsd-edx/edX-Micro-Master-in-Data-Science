"""
The function find_matches takes as input two parsed and evaluated trees, one for the correct answer and one for the attempt.
It finds the subexpressions that match between the correct and the attempt and returns it as a list of 
tuples of the form (node,value,answer_part,attempt_part)

The other functions are helpers that are called from find_matches.
"""
import sys
from collections import deque
from string import strip, replace
import json
from hint_class_helpers.find_matches import find_matches

#from webwork_parser import parse_webwork

# Set up a logging object
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
#logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

def common_subexpressions(params):
    final_pairs=find_matches(params)
        if len(final_pairs)>0:
            for node,value,ans_piece,attempt_piece in final_pairs:
                if value>10 or value != int(value):
                    # print hint
                    if node=='R': # attempt is correct
                        sub_type='answer'
                    else:
                        sub_type='sub-expression'
                    if attempt_piece != ans_piece:
                        return 'The {0} {1} is correct, it could also be written as {2}'.format(sub_type,attempt_piece,ans_piece)
                    else:
                        return 'The {0} {1} is correct'.fromat(sub_type,attempt_piece)



if __name__=="__main__":
    sys.path.append('../src')
    from parsetrees.expr_parser.Eval_parsed import parse_and_eval
    from collections import Counter

    if len(sys.argv)==3:   #parameters are two expressions
        params={}
        params['answer']=sys.argv[1]
        params['attempt']=sys.argv[2]
        params['ans_tree']=parse_and_eval(params['answer'])
        params['att_tree']=parse_and_eval(params['attempt'])
        print 'params=',params
        final_pairs=find_matches(params)
        for item in final_pairs:
            print "node=%s, value=%s, The piece %s in your answer is correct, it can also be expressed as %s"%(item[0],item[1],item[3],item[2])

    elif len(sys.argv)==2: # param is the name of a file containing a dump of attempts with their parse trees and variables
        file=open(sys.argv[1],'r')
        print file.readline()
        print file.readline()

        Clusters=Counter()
        Reps={}
        i=1
        for line in file.readlines():
            i+=1
            if len(line)>1000:
                print 'long line error in line',i
                continue
            print line,
            params=json.loads(line)
            print 'params=',params
            params['attempt'] = ''.join(params['attempt'].split()) # remove whitespaces
            if params['ans_tree']==None:
                print '-'*50,'error parsing answer'
                params['ans_tree']=parse_and_eval(params['answer'])
            final_pairs=find_matches(params)
            if len(final_pairs)>0:
                for node,value,ans_piece,attempt_piece in final_pairs:
                    if value>10 or value != int(value):
                        #Update clusters
                        if not node in Reps.keys():
                            Reps[node]=ans_piece
                        Clusters[node]+=1
                        # print hint
                        if node=='R': # attempt is correct
                            sub_type='answer'
                        else:
                            sub_type='sub-expression'
                        if attempt_piece != ans_piece:
                            print 'The %s %s is correct, it could also be written as %s'%(sub_type,attempt_piece,ans_piece)
                        else:
                            print 'The %s %s is correct'%(sub_type,attempt_piece)
                    else:
                        Clusters['Nothing']+=1
            else:
                Clusters['Nothing']+=1


        print 'Clusters='
        print 'Nothing recognizable=',Clusters['Nothing']
        for node in Reps.keys():
            print "%20s%30s%10d"%(node,Reps[node],Clusters[node])
