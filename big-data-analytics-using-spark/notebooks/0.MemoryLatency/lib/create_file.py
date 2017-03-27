import time

stat=open('stats.txt','w')

def tee(line):
    print line
    stat.write(line+'\n')
    
def create_file(n,m,filename='DataBlock'):
    """Create a scratch file of a given size

    :param n: 
    :param m: 
    :param filename: 
    :returns: 
    :rtype: 

    """
    t1=time.time()
    A=bytearray(n)
    t2=time.time()
    file=open(filename,'w')
    for i in range(m):
        file.write(A)
        if i % 100 == 0:
            print i,",",
    file.close()
    t3=time.time()
    tee('\ncreating %d byte block: %f sec, writing %d blocks %f sec' % (n,t2-t1,m,t3-t2))
    return (t2-t1,t3-t2)
