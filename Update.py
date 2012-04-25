#!/usr/bin/python

import sys, os, shutil, platform, subprocess
import glob, re

for filename in glob.glob('*/*.xcodeproj/project.pbxproj'):
    print filename
 
    # Slurp the file   
    projectfile = open(filename, 'r')
    contents = projectfile.read()
    projectfile.close()
    
    # Make the update
    contents = contents.replace("iphoneos3.1", "iphoneos4.0")
    
    # Spit the file back out
    projectfile = open(filename, 'w')
    projectfile.write(contents)
    projectfile.close()
