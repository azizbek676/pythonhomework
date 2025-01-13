def add_underscore(txt):
    vowels = 'aeiouAEIOU'
    result = []
    count = 0

    for i in range(len(txt)):
        
        if txt[i] in vowels or (i > 0 and txt[i-1] == '_'):
            result.append(txt[i])
        else:
            count += 1
            result.append(txt[i])
            
            if count == 3 and i != len(txt) - 1:
                result.append('_')
                count = 0
    
    return ''.join(result)

txt = "abcdefghijklm"
print(add_underscore(txt))