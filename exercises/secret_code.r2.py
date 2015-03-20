import sys
import cipher 
from morse.morse_input import get_morse_word

verbose=True

raw_keyword   = sys.argv[1]
operation     = sys.argv[2]
filename      = sys.argv[3]

# checking to make sure 2nd argument is correct.
if (operation!='encode') and (operation !='decode'):
  print "invalid operation...use 'encode' or 'decode'" 

if raw_keyword=='morse':
  print "getting keyword from telegraph"
  raw_keyword=get_morse_word()

print 'keyword = '+str(raw_keyword)
#removing duplicate letters and capitalizing all letters
letter_array=[]

# iterating through each letter of uppercase letter array.
for letter in raw_keyword.upper(): 
  # removing duplicates.
  if letter not in letter_array:
    letter_array.append(letter)

keyword=''.join(letter_array)
print keyword
print 'encoded as: ' + keyword;

encode_map,decode_map=cipher.create_cipher(keyword)

# printing out encoding map 
if verbose:
  alphabet=[chr(65+i) for i in range(26)]
  if operation=='encode':
    for letter in alphabet:
      print letter + ' -> ' + encode_map[letter]   
  if operation=='decode':
    for letter in alphabet:
      print letter + ' -> ' + decode_map[letter]
  print "======================="
#opening file and reading contents    
fin=open(filename,'r')
text=fin.read()
fin.close()

#using encode_message to encode or decode
if operation=='encode':
  transformed_text=cipher.encode_message(text,encode_map,verbose)
if operation=='decode':
  transformed_text=cipher.encode_message(text,decode_map,verbose)
   
#writing to file   
fout=open(filename+'.'+operation+'d','w')
fout.write(transformed_text)
fout.close()

print "wrote output to "+filename+'.'+operation+'d'     

