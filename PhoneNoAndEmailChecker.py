import pyperclip ,re


phonenoRe=re.compile(r'''((
        (\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?)
        |(([+]{1})   #indian phone number
        ([9])?     #start with 9
        ([0123456789]{11})   #rest 11 digits
        )|\d{8})''',re.VERBOSE|re.IGNORECASE|re.DOTALL)




emailRe=re.compile(r'''(
        \w+     #username
        @
       \w+        #domain name
        (\.[a-zA-Z]{2,4})
        )''',re.VERBOSE)



#coping from the clipboard
text=str(pyperclip.paste())
matches=[]
matches=phonenoRe.findall(text)
#pyperclip.copy(matches)

email=[]
email= emailRe.findall(text)
#pyperclip.copy(email)

elen=len(email)
for i in range (0,elen):
   print(email[i][0])

plen=len(matches)
for i in range (0,plen):
    print(matches[i][0])


#print(matches)
#print(email)
