def characterLocator(word,character):
    index=[];
    offset=-1;
    while True:
        offset=word.find(character,offset+1);
        if(offset==-1):
            break;
        else:
            index.append(offset);
    if((index.__len__())==0):
        return -1;
    else:
        return index;
# input_word=input("input your line: ");
# input_character=input("input your search character: ");
# result=characterLocator(input_word,input_character);
# if(result==-1):
#     print("your character not found");
# else:
#     print(result);
            
    
