def multiplyTable(number):
    table=[];
    temp=[];
    i=1;
    while i<=number:
        j=1;
        while j<=i:
            temp.append(i*j);
            j+=1;
        i+=1;
        table.append(temp);
        temp=[];
    return table;
# num=input("enter your number: ");
# t=multiplyTable(int(num));
# print(t);
