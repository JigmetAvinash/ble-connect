Resourcefile = open("resource.txt", "r+")

print("Output of Read function is ")
txt = Resourcefile.readlines()
print(txt)

unwantedtext = "\n"
txt1 = [] 

for i in txt[1]:
    if i == unwantedtext:
        txt[1] = txt[1].strip(unwantedtext)
        print(txt) 
for i in txt[2]:
    if i == unwantedtext:
        txt[2] = txt[2].strip(unwantedtext)
        print(txt)

    
