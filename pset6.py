# Problem 1 : Build the Shift Dictionary and Apply Shift
class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #pass #delete this line and replace with your code here
        str1='abcdefghijklmnopqrstuvwxyz'
        str2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d={}
        for i in str1:
            d[i]=str1[(str1.index(i)+shift)%26]
        for i in str2:
            d[i]=str2[(str2.index(i)+shift)%26]
        return d

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #pass #delete this line and replace with your code here
        str4=''
        str3= self.message_text
        str1='abcdefghijklmnopqrstuvwxyz'
        str2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d={}
        for i in str1:
            d[i]=str1[(str1.index(i)+shift)%26]
        for i in str2:
            d[i]=str2[(str2.index(i)+shift)%26]
        for i in str3:
            if i in 'abcdefghijklmnopqrstuvwxyz' :
               str4+=d[i]
            elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
               str4+=d[i] 
            else:
               str4+=i
        return str4
        
        
        
        
# Problem 2 : PlaintextMessage
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        #pass #delete this line and replace with your code here
        Message.__init__(self,text)
        self.shift=shift
        self.text = text
        self.encrypting_dict=Message.build_shift_dict(self,shift)
        self.message_text_encrypted=Message.apply_shift(self,shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        #pass #delete this line and replace with your code here
        return self.shift
    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        #pass #delete this line and replace with your code here
        c = {}
        a = self.encrypting_dict.keys()
        for i in a:
            c[i] = self.encrypting_dict[i]
        return c
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        #pass #delete this line and replace with your code here
        return self.message_text_encrypted
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        #pass #delete this line and replace with your code here
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)
        
        
        
# Problem 3 : CiphertextMessage
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #pass #delete this line and replace with your code here
        Message.__init__(self,text)
        #self.valid_words=load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #pass #delete this line and replace with your code here
        c=0
        message_answer=''
        message=''
        count=0
        ans=0
        count_old=0
        for c in range(0,27):
           count=0
           message=Message.apply_shift(self,26-c)
           msg=message.split(' ')
           for i in msg:
              if i in self.valid_words:
                 count=count+1
           if count>ans:
              ans=count
              message_answer=message
              ans=c
        return (26-ans,message_answer) 
        
        
        
# Problem 4 : Decrypt a Story
def decrypt_story():
    obj=CiphertextMessage(get_story_string())
    t=obj.decrypt_message()
    return t
