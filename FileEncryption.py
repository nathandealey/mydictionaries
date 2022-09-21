
infile = open("info_security.txt", 'r')
for line in infile:
    text = line

codes = {

}



newtext = ""

for i in range(0, len(text)):
    if text[i] in codes.keys():
        newtext += codes[text[i]]
    else:
        newtext += text[i]

print(newtext)

outfile = open('encrypted.txt', 'w')
outfile.write(newtext + '\n')

outfile.close()