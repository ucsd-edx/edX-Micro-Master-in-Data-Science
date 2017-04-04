#!/usr/bin/env python

import re
import os
import sys

def convertMdtoIMD(srcFileName, desFileName):
    desDir = '.'
    imdName = desFileName
    lastSlashPos = desFileName.rfind(r'/')
    if lastSlashPos != -1:
        desDir = desFileName[:lastSlashPos + 1]
        imdName = desFileName[lastSlashPos + 1 : ]
    print imdName
    if imdName in os.listdir(desDir):
        "imd file " + imdName + "exits, overlap? n/y"
        overlap = raw_input("imd file " + imdName + " exits, overlap? n/y : ")
        if overlap is 'n':
            return

    srcFo = open(srcFileName, 'r')
    desFo = open(desFileName, 'w')
    for eachLine in srcFo:
        desLine = eachLine
        desLine = re.sub('\$', r'\\$', desLine)
        desLine = re.sub(r'\\\\\\\(', r'$', desLine)
        desLine = re.sub(r'\\\\\\\)', r'$', desLine)
        desLine = re.sub(r'\\\\\\\[', r'$$', desLine)
        desLine = re.sub(r'\\\\\\\]', r'$$', desLine)
        desFo.write(desLine)

def convertAll(currDir):
    for item in os.walk(currDir):
        eachDir = item[0]
        fileList = item[2]
        for eachFile in fileList:
            if eachFile[-3:] == r'.md' and eachFile != r'README.MD':
                srcFileName = os.path.join(eachDir, eachFile)
                desFile = eachFile[:-2] + r'imd'
                desFileName = os.path.join(eachDir, desFile)
                convertMdtoIMD(srcFileName, desFileName)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        currDir = sys.argv[1]
        convertAll(currDir)
    if len(sys.argv) == 3:
        srcFileName = sys.argv[1]
        desFileName = sys.argv[2]
        convertMdtoIMD(srcFileName, desFileName)
