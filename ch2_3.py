phrase = "Dont' panic!"

#on tap 
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase+''.join([plist[5],plist[3],plist[7],plist[6]])

print(plist)
print(new_phrase)
