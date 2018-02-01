def calcArea(shape,dim1,dim2=0):
    if(dim2==0):
        if(shape=="s"):
            return dim1*dim1;
        elif(shape=="c"):
            return 3.14*dim1*dim1;
    else:
        if(shape=="r"):
            return dim1*dim2;
        elif(shape=="t"):
            return 0.5*dim1*dim2;
# area=calcArea("t",10,7);
# print(area);
# area=calcArea("r",10,7);
# print(area);
# area=calcArea("s",10);
# print(area);
# area=calcArea("c",10);
# print(area);
