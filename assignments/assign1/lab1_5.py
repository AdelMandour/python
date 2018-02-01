def dictionary(list):
    dictionary={};
    for word in list:
        try:
            name=dictionary[word[0]];
        except:
            name=[];
        name.append(word);
        dictionary[word[0]]=name;
    return dictionary;
# l=["zinab","wael","ahmed","fatma","ibrahim","ali","islam"];
# d=dictionary(l);
# print(d);
