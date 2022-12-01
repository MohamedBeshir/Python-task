
import re
	
def tokenizer(data):
    current=0
    tokens=[]
    keywords=['main','int','void','for','while','do','if','else','break','char']
    alphabet=re.compile(r"[a-z]|_|\d")
    numbers=re.compile(r"\.|\d")
    whitespace=re.compile(r"\s")
    operators=re.compile(r"[+,\-,*,/,&,^,|,%,^,>,<,~,!,=]")
    special_char=re.compile(r"[#,(,),{,},?,:,;,\',\",\\,\[,\],\,]")

    while current < len(data):
        char = data[current]
        if re.match(whitespace, char):
            current = current +1
            continue
        if re.match(special_char,char):
            tokens.append(char)
            current=current+1
            continue
        if re.match(operators, char):
            value=''
            while re.match(operators, char):
                value += char
                current = current +1
                char= data[current]
            tokens.append(value)
            continue
        if re.match(numbers, char):
            value=''
            while re.match(numbers, char):
                value += char
                current = current +1
                char= data[current]
            tokens.append(value)
            continue
        if re.match(alphabet, char):
            value=''
            while re.match(alphabet, char):
                value += char
                current = current +1
                char= data[current]
            if value in keywords:
                tokens.append(value)
            else:
                tokens.append(value)
            continue
        current=current+1
    print(tokens)




main=''' while(num!=0)
    {
        _j_20 300 = num % 10.000;
        for (i = 0; i < 16; i++)
        {
            if (arr[i] == j)
            {
                if (i < 10)
                {
                    hexa[n] = (char)(i + 48);
                }
                else
                {

                    hexa[n] = (char)((i - 10) + 65);
                }
                break;
            }
       }
        num /= 10000;
        n++;
    }'''
tokenizer(main)

