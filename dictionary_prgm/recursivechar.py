# pattern="ABACCD"
# char_repeat={}
# for char in pattern:
#     if char in char_repeat:
#         print(f"first recursive is {char}")
#         break
#     else:
#         char_repeat[char]=1


pattern="ABAABCCD"
char_repeat={}
recusive_char=[]
for char in pattern:
    if char in char_repeat:
        recusive_char.append(char)
    else:
        char_repeat[char]=1
print(recusive_char[1],"second recusive")




