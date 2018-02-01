def vowelsRemover(word):
    vowels=('a','e','i','o','u','A','E','I','O','U');
    string="";
    for i in word:
        if(not (i in vowels)):
            string+=i;
    return string;

def vowelsRemoverlist(arr):
    vowels=('a','e','i','o','u','A','E','I','O','U');
    string="";
    unvowels=[];
    for word in arr:
        for i in word:
            if(not (i in vowels)):
                string+=i;
        unvowels.append(string);
        string=""
    return unvowels;
        

# input=input("enter your line: ");
# vr=vowelsRemover(input);
# print(vr);

# list=["mobile","car","labtop"];
# vrl=vowelsRemoverlist(list);
# print(vrl);
