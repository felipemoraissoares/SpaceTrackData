##
## Simple Python projetct to obtain data of objects in space orbit from www.space-track.org
## This data will be saved in a csv file according to the space-track api query
## The information is acquired from a set query made at https://www.space-track.org/#/queryBuilder
## The results are the latest TLE's, in Json format
## The site credentials, query informations and outputs files can be changed in args.py
##

from datatracker import datatracker

if __name__ == '__main__':
    datatracker()