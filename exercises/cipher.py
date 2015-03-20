def create_cipher(keyword):
  """This function will take a correctly formed keyword
  and build substitution maps (dictionaries) for encoding and decoding 
  text."""

  # creating an alphabet as an array of letters
  alphabet=[]
  for i in range(26): alphabet.append(chr(65+i))
  alphabet_full=alphabet[:] #making a copy that will not be altered

# simultaneously creating an encoder and decoder
  encode_map={};
  decode_map={};
  
  # the keyword is the first portion of the map.  For keyword='cat', 
  # the first three letters of the encode map are a->c, b->a, c->t
  # c,a,t are then removed from the alphabet for the remaining substitutions.
  # an inverse map is created simultaneously with the values reversed.
  for i_orig, new_letter in enumerate(keyword):  #using the keyword as the first set of letters
     orig_letter = alphabet_full[i_orig]
     encode_map[ orig_letter ] = new_letter
     decode_map[ new_letter ]  = orig_letter
     alphabet.remove(new_letter)  #removing this letter from the mapping
  
  # the next section uses the remaining letters of the alphabet and subsittutes
  # sequentially.
  for i_new,new_letter in enumerate(alphabet):  
     i_orig += 1
     orig_letter = alphabet_full[i_orig]
     encode_map[orig_letter] = new_letter
     decode_map[new_letter]  = orig_letter
  return encode_map,decode_map     


def encode_message(text,letter_map,verbose):
  """this function will take a text string and a letter mapping, and make the 
  necessary substiutions based on the map.  Capitals are accounted for, and 
  punctuation does not affect the method."""

  cipher_text_array = [] #creating an appendable array
  cipher_text = ''
  for i_letter,letter in enumerate(text):
    if letter in letter_map.keys():   # looking for uppercase letter match
      new_letter = letter_map[letter] # assigning remapped letter
    elif letter.upper() in letter_map.keys(): # looking for lowercase match
      new_letter = letter_map[letter.upper()].lower() # assigning lowercase match
    else:
      new_letter = letter
    
    cipher_text += new_letter
    if verbose: print letter+' -> '+ new_letter  

  return cipher_text
  
  
