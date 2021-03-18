#!/usr/bin/python
#20200925 By fujch  Mail fujch@foxmail.com
#This code is for processing rnammer with multiple species 
import os
import getopt
import sys
opts,args = getopt.getopt(sys.argv[1:],'-i:',['inputpath='])
for opt_name,opt_value in opts:
	if opt_name in ('-i','--inputpath'):
   	   path1 = '/home/rnammer/input/'+opt_value
           path2 = '/home/rnammer/output/'+opt_value
if not os.path.exists(path2):
   os.makedirs(path2)
files = os.listdir(path1)
for file in files:
    ifile = os.path.splitext(file)[0]
    ifile_str = str(ifile)
    ofile_str = ifile_str[0:-8]+"_16S_genomic.fas"
    os.system("perl rnammer -S bac -m ssu -f %s/%s - < %s/%s" %(path2,ofile_str,path1,file))