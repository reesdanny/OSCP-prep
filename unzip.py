#unzips all files to one directory

import os                                                                                                      
import fnmatch
import zipfile


sourceFolder = "/"
targetUnzippedFolder = "/"

for root, dirs, files in os.walk(sourceFolder):
    for filename in fnmatch.filter( files, "*.zip" ):
        print "   " + os.path.join(root, filename)
        zipfile.ZipFile( os.path.join(root, filename) ).extractall( targetUnzippedFolder )
