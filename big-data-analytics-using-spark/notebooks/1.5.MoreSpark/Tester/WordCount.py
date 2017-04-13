import pickle

from Tester2 import *
import re 

def getkmers(text_file, l,k, map_kmers, count_kmers, sort_counts):
    # text_file: the text_file RDD read above
    # l: will print the l most common 3mers
    
    # Do Not modify this function
    def removePunctuation(text):
        return re.sub("[^0-9a-zA-Z ]", " ", text)
    text = text_file.map(removePunctuation)\
                    .map(lambda x: x.lower())
    singles=map_kmers(text,k)
    count=count_kmers(singles)
    sorted_counts=sort_counts(count)
    return sorted_counts
    
def exercise(pickleFile, map_kmers, count_kmers, sort_counts, sc):
    text_file = sc.textFile(u'../../Data/Moby-Dick.txt')
    data = getPickledData(pickleFile)
    case = data['ex4']['outputs'][0]
    func_student = lambda RDD: getkmers(RDD, 5,3, map_kmers, count_kmers, sort_counts)
    TestRDDK( data=text_file, func_student=func_student, corAns=case[0], corType=case[1], takeK=5)
    print 