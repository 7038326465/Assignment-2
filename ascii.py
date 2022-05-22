# Check the bellow program for Alphabet as a key & ascii value as values.


# check the program for aplphabet as a key and values as a ascii values.
Asciidict=dict( )
alphaletter=range(97,123)
for i in alphaletter:
    Asciidict[chr(i)]=str(i )
    
    print(Asciidict,end='')
