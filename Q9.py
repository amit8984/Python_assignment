import os, sys

path=input()
dirs=os.listdir( path )

for file in dirs:
    print(file)
