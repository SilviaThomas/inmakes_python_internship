#match
import re
pattern="python"

if re.match(pattern,"hello python  ygdgghhfdesdfvh"):
    print("matched")
else:
    print("not matched")

#search
import re
pattern="python"

if re.search(pattern,"hello python.how are youuu  ygdgghhfdesdfvh"):
    print("matched")
else:
    print("not matched")

#findall
import re
pattern="python"
print((re.findall(pattern,"hello i am python,python is a future tech,python is one of the popular language")))

#find and replace
import re
str="hai inmakes,hello india"
pattern="hello"
new=re.sub(pattern,"inmakes",str)
print(new)

#dotmeta character
import re
pattern="r.d"
if re.match(pattern,"rqd"):
    print("correct")
else:
    print("not correct")

#character class
import re
pattern="[A-Z][0-9][a-z]"
if re.search(pattern,"P9u"):
    print("matched")
else:
    print("not matched")