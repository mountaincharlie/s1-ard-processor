import logging
import luigi
import os
import shutil
from datetime import datetime
from os.path import basename, join
from luigi.contrib.s3 import S3Target, S3Client
from workflow_common.s3 import getBucketNameFromS3Path, getPathFromS3Path
from luigi import LocalTarget

def getS3Target(key):
    client = S3Client()
    return S3Target(path=key, client=client)

def getLocalTarget(key):
    return LocalTarget(key)

def getLocalStateTarget(targetPath, fileName):
    targetKey = join(targetPath, fileName)
    return getLocalTarget(targetKey)

def getS3StateTarget(targetPath, fileName):
    targetKey = join(targetPath, fileName)
    return getS3Target(targetKey)

def getProductIdFromSourceFile(sourceFile):
    productFilename = basename(sourceFile)
    return '%s_%s_%s_%s' % (productFilename[0:3], productFilename[17:25], productFilename[26:32], productFilename[42:48])

def getProductPatternFromSourceFile(sourceFile):
    productFilename = basename(sourceFile)
    return '%s_%s%s%s_%s_%s' % (productFilename[0:3], productFilename[23:25], datetime.strptime(productFilename[21:23], '%m').strftime('%b'), productFilename[17:21], productFilename[26:32], productFilename[42:48])

def createTestFile(outputfile):
    os.makedirs(os.path.dirname(outputfile), exist_ok=True)
    with open(outputfile, 'w') as f:
        f.write('TEST_FILE')


def createWorkingnewPath(workingPathRoot, workingPath): 
    newPath = os.path.join(workingPathRoot, workingPath)

    if (os.path.exists(newPath)):
        #empty out the structure
        for f in os.listdir(newPath):
            path = os.path.join(newPath, f)

            if os.path.isfile(path):
                os.unlink(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
    else:
        if not os.path.exists(newPath):
            os.makedirs(newPath)

    return newPath


            