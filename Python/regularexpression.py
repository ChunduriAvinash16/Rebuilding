import re
pattern="Avinash"
s="Hello Good morning,Avinash"
print("Match will return true if found else return None")
print("re.match() will try to find at the beginning")
print("Found") if(re.match(pattern,s)) else print("Not Found")

print("Search is successful return True else return None")
print("re.search() search for pattern any where in the string")
print("Found") if(re.search(pattern,s)) else print("Not Found")

s="Hello hello hello Good Morning every one"
repl="Hi"
print(re.sub("Hello",repl,s,flags=re.I))

#findall
pattern=r"[a-zA-z]+ \d+"
s1="LXI 203,ABC 111,abcd 1234,Hello 1234 Everyone"
matches=re.findall(pattern,s1)
for match in matches:print(match,end=" ")

#finditer
matches=re.finditer(pattern,s1)
print(matches) #iter object
for match in matches:
  print(match.start())
  print(match.end())
  print(match.span())