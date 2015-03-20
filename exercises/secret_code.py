import sys
import cipher 
verbose=True

raw_keyword       = sys.argv[1]
operation         = sys.argv[2]
filename          = sys.argv[3]
verbose_setting   = "quiet"
if len(sys.argv)==5:
  verbose_setting  = sys.argv[4]



verbose_flag=False
if verbose_setting=='verbose': verbose_flag=True

# checking to make sure 2nd argument is correct.
if (operation!='encode') and (operation !='decode'):
  print "invalid operation...use 'encode' or 'decode'" 

print 'keyword = '+str(raw_keyword)
#removing duplicate letters and capitalizing all letters
letter_array=[]

# iterating through each letter of uppercase letter array.
for letter in raw_keyword.upper(): 
  # removing duplicates.
  if letter not in letter_array:
    letter_array.append(letter)

keyword=''.join(letter_array)
print 'encoded as: ' +keyword;

encode_map,decode_map=cipher.create_cipher(keyword)

# printing out encoding map 
if verbose_flag:  print "the Cipher looks like this: "
if verbose:
  alphabet=[chr(65+i) for i in range(26)]
  if operation=='encode':
    for letter in alphabet:
      if verbose_flag:  print letter + ' -> ' + encode_map[letter]   
  if operation=='decode':
    for letter in alphabet:
      if verbose_flag:  print letter + ' -> ' + decode_map[letter]
  if verbose_flag:  print "======================="
#opening file and reading contents    
fin=open(filename,'r')
text=fin.read()
fin.close()

#using map_letters to encode or decode
if operation=='encode':

  print "Encoding " + filename
  transformed_text=cipher.encode_message(text,encode_map,verbose_flag)
if operation=='decode':
  print "Decoding " + filename
  transformed_text=cipher.encode_message(text,decode_map,verbose_flag)
   
#writing to file   
fout=open(filename+'.'+operation+'d','w')
fout.write(transformed_text)
fout.close()

print "wrote output to "+filename+'.'+operation+'d'     
     
