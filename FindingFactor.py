num=int(input("Input a number : "));
temp=2;
while temp<=num:
    if(num%temp==0):
        if(num/temp==1):
            print(temp,end="");
            num=1;
        else:
            print(temp,"x",end=" ");
            num/=temp;
            temp=2;
    else:
        temp+=1;
