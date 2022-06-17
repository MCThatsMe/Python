#import unicodedata
#str = unicodedata(str, errors='ignore')
filename = "C:\\Users\\MC\\Desktop\\Code\\Python\\eBooks\\Alice in Wonderland.txt"
with open(filename, encoding="latin-1") as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))
