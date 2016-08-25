# PROBLEM 1 : 
def dict_invert(d):
    d2=dict()
    for i in d:
        d2.setdefault(d[i],[]).append(i)
    for i in d2:
        d2[i].sort()
    return d2
    
    
# PROBLEM 2 part 1:
def getSublists(L, n):
    ans=[]
    for i in range(0,len(L)-n+1):
        lt=[]
        for j in range(i,i+n):
            a=L[j]
            lt.append(a)
        ans.append(lt)
    return ans
  
# PROBLEM 2 part 2:
def longestRun(L):
    ans=0
    c=1
    for i in range(0,len(L)):
        c=1
        for j in range(i,len(L)-1):
           if L[j]<=L[j+1]:
               c=c+1
           else:
               break
        if c>ans:
            ans=c         
    return ans
    
    
    

# PROBLEM 3 : 
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        # Write your code here
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
        if status=='citizen' or status=='legal_resident' or status=='illegal_resident':
            self.status=status
        else:
            raise ValueError
        
    def getStatus(self):
        """
        Returns the status
        """
        # Write your code here
        return self.status
        
        
        
# PROBLEM 4 PART 1 :
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: '+ self.lecture(stuff)
    def lecture(self, stuff): 
        return 'It is obvious that ' + Person.say(self,stuff)
 
# PROBLEM 4 PART 2 :
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: '+ self.lecture(stuff)
    def lecture(self, stuff): 
        return 'It is obvious that ' + Lecturer.lecture(self,stuff)
        
# PROBLEM 4 PART 3 :
class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. '+self.name + ' says: ' + self.lecture(stuff)
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff) 


