'''def getdiffreance(a,b):
    if isinstance(a,float):
       return a-b;

#print("hi")
#a=5.5;
#b=5.5;
#c=getdiffreance(a,b)
#print(c)'''


def getvalues(a, pi=3.141, c=None):
    if c is not None:
        print(c)
        return a + pi + c
    return a + pi


print("hi")
if __name__ == '__main__':
    print(getvalues(4))
    print(getvalues(4, 10))
    print(getvalues(4, 10,20))
