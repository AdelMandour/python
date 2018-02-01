def arc(number):
    i=0;
    string="";
    draw=[];
    while i<number:
        j=0;
        while j<=i:
            string+="*"
            j+=1;
        draw.append(string);
        string="";
        i+=1;
    empty="";
    k=1;
    primad=[];
    for i in draw:
        j=number-k;
        while j>0:
            empty+=" ";
            j-=1;
        primad.append(empty+i);
        empty="";
        k+=1;
    return primad;
# num=input("enter the level of * ");
# s=arc(num);
# for i in s:
#     print(i);
# for i in range(int(number)):
#     print(" "*(int(number)-1-i)+"*"*(i+1));