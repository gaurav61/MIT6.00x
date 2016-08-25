# PROBLEM 1 : Radiation Exposure
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    ans=0.0
    i=start
    while i<stop:
        ans=ans+(step*f(i))
        i=i+step
    return ans
    
    
# PROBLEM 2 : Hangman Part 1: Is the Word Guessed
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
      if i not in lettersGuessed:
        return False
    return True
    
    
# PROBLEM 3 : Printing Out the User's Guess
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    srr=''
    for i in secretWord:
        if i not in lettersGuessed:
            srr=srr+'_ '
        else:
            srr=srr+i+' '
            
            
# PROBLEM 4 : Printing Out all Available Letters
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    srr=''
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in lettersGuessed:
            srr=srr+i
    return srr
    
  
# PROBLEM 5 : Hangman Part 2: The Game/Complex Tests
def getAvailableLetters(lettersGuessed):
    srr=''
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in lettersGuessed:
            srr=srr+i
    return srr
def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
      if i not in lettersGuessed:
        return False
    return True
    
def isWordGuessed2(secretWord, lettersGuessed):
    for i in secretWord:
      if i  in lettersGuessed:
        return True
    return False
    
def getWordGuessed(secretWord, lettersGuessed):
    srr=''
    for i in secretWord:
        if i not in lettersGuessed:
            srr=srr+'_ '
        else:
            srr=srr+i
            
    return srr    
           
def hangman(secretWord):
    flag=0
    print ('Welcome to the game, Hangman!')
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long'
    print('-------------')
    g=8
    l=[]
    while g>0:
        print 'You have '+str(g)+' guesses left'
        print 'Available Letters: '+getAvailableLetters(l)
        opt=raw_input('Please guess a letter: ')
        opt=opt.lower()
        if opt in l:
            print 'Oops! You\'ve already guessed that letter: '+getWordGuessed(secretWord,l)
            print('-------------')
            continue
        l.append(opt)
        if isWordGuessed2(secretWord,l[len(l)-1:len(l)])==True:
            print 'Good guess: '+getWordGuessed(secretWord,l)
            print('-------------')
        else:
            print 'Oops! That letter is not in my word: '+getWordGuessed(secretWord,l)
            print('-------------')
            g-=1
        if isWordGuessed(secretWord,l)==True:
            flag=1
            break
    if flag==1:
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was '+secretWord

