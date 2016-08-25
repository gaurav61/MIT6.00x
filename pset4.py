# PROBLEM : 1 Word Scores
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    s=0
    for i in word:
        s=s+SCRABBLE_LETTER_VALUES[i]
    s=s*len(word)
    if len(word)==n:
        s+=50
    return s
    
    
# PROBLEM : 2 Dealing with Hands
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand1=hand.copy()
    for i in word:
        if hand1.get(i,0)!=0:
            hand1[i]=hand1[i]-1
    return hand1
    
   
# PROBLEM : 3 Valid Words
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand1=hand.copy()
    if word not in wordList:
        return False
    for i in word:
     if hand1.get(i,0)>0:
        if hand1[i]<=0:
            return False
        else:
            hand1[i]=hand1[i]-1
     else:
         return False
    return True 
    
    
# PROBLEM : 4 Hand Length
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    count=0
    for i in hand:
        if hand[i]>0:
           count=count+hand[i]
    return count
    

# PROBLEM : 5 Playing a Hand  
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    ans=0
    while calculateHandlen(hand)>0:
        print "Current Hand: ", displayHand(hand)
        word=raw_input("Enter word, or a \".\" to indicate that you are finished: ")
        if word=='.':
            print "Goodbye! Total score: "+str(ans)+" points."   
            break
        if isValidWord(word, hand, wordList)==False:
            print "Invalid word, please try again."
            continue
        ans=ans+getWordScore(word,n)
        print "\""+word+"\""+"earned "+str(getWordScore(word,n))+" points. Total: "+str(ans)+" points"
        hand=updateHand(hand, word)
    if calculateHandlen(hand)==0:
         print "Run out of letters. Total score: "+str(ans)+" points"
         
         
# PROBLEM : 6  Playing a Game
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    flag=0
    while True:
        op=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if op=='r':
            if flag==0:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                playHand(hand, wordList, HAND_SIZE)              
        elif op=='n':
            flag=1
            hand=dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            
        elif op=='e':
            break
            
        else:
            print "Invalid command."
            
            
# PROBLEM : 7 Computer Chooses a Word
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)
    score=0
    ma=-1
    st=None
    for i in wordList:
        if isValidWord(i, hand, wordList)==True:
           score= getWordScore(i, n)
           if score>ma:
               st=i
               ma=score
    # Create a new variable to store the best word seen so far (initially None)  
    return st
    
    
# PROBLEM : 8  Computer Plays a Hand
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)
    score=0
    ma=-1
    st=None
    for i in wordList:
        if isValidWord(i, hand, wordList)==True:
           score= getWordScore(i, n)
           if score>ma:
               st=i
               ma=score
    # Create a new variable to store the best word seen so far (initially None)  
    return st

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... 
    total=0
    temp=0
    while True:
      if calculateHandlen(hand) > 0:
          print "Current Hand: ",
          displayHand(hand) 
      word=compChooseWord(hand, wordList, n)
      if word==None:
          print "Total score: "+str(total)+" points"
          return None   
      temp=getWordScore(word, n)    
      total=total+temp
      print "\""+word+"\""+" earned "+str(temp)+" points. Total: "+str(total)+" points"
      print
      hand=updateHand(hand, word)
    print "Total score: "+str(total)+" points"
    
    
    
# PROBLEM : 9  You and your Computer
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    flag=0
    while True:
        op=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if op=='n':
            flag=1
            hand=dealHand(HAND_SIZE)
            while True:
                
               op2=raw_input('Enter u to have yourself play, c to have the computer play: ')
               if op2=='u':
                       playHand(hand, wordList, HAND_SIZE)    
                       break
               elif op2=='c':
                   compPlayHand(hand, wordList, HAND_SIZE)
                   break
               else:
                   print 'Invalid command.'
        elif op=='r': 
               if flag==0:
                   print 'You have not played a hand yet. Please play a new hand first!'
               else:
                   op2=raw_input('Enter u to have yourself play, c to have the computer play: ')
                   if op2=='u':
                       playHand(hand, wordList, HAND_SIZE)    
                   elif op2=='c':
                       compPlayHand(hand, wordList, HAND_SIZE)
                   else:
                       print 'Invalid command.'
            
        elif op=='e':
                break
        else:
             print 'Invalid command.'


