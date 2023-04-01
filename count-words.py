accpetable_words=['i','we','he','it']
with open('essay.txt','r') as f:
    lst=[]
    data = f.read()
    words=data.split()
    for x in words:
        if (x.lower() in accpetable_words) :
            lst.append(x)
        else:
            if (len(x)>2):
               lst.append(x)



    print(len(lst))