import re
pat=re.compile(r'([\s|(\d)+-]+)([\.A-Z].*)')
def plan2table(debugString,length=70):
    """
    The plan2table helper function takes as input the output of the spark planner printer:
    RDD.toDebugString()
    and output a string that, when copied to a markdown cell in jupyter, creates a
    table that is more readable and annotatbale
    """
    header="""
| Execution plan   | RDD |
| :---------------------------------------------------------------- | :------------: |"""
    print(header)
    for line in debugString.splitlines():
        line=line.decode()
        m=pat.match(line)
        if m:
            pre,post=m.groups()
            pre=pre.replace(' ','_')
            pre=pre.replace('|','/')
            recon=pre+post
            print('|`%s`| rdd |'%recon[:70])
        else:
            print("can't parse line")
            print(line)
            