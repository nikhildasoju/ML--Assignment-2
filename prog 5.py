str='The quick Brow Fox'
u=0
l=0
for i in str:
    if(i!=' ' and i.isupper()):
        u+=1
    elif(i!=' ' and i.islower()):
        l+=1
print("No.of Upper-case charecters:",u)
print("No.of Lower-case Charecters:",l)