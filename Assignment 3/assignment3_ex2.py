def generateSentence(characters,n,str):
    if n==0:
        print(str)
        return
    
    for i in characters:
        generateSentence(characters,n-1,str+i)

characters=["a","b","c"]
n=3


generateSentence(characters,n,"")