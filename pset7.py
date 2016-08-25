# PROBLEM 1 : The Adoption Center
class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        # Your Code Here
        self.name=name
        self.species_types=species_types
        self.location=location
    def get_number_of_species(self, animal):
        # Your Code Here
        try:
            return self.species_types[animal]
        except:
            return 0
    def get_location(self):
        # Your Code Here
        a=float(self.location[0])
        b=float(self.location[1])
        return (a,b)
    def get_species_count(self):
        # Your Code Here
        d=self.species_types.copy()
        return d
    def get_name(self):
        # Your Code Here
        return self.name
    def adopt_pet(self, species):
        # Your Code Here
        flag=0
        try:    
            if self.species_types[species]<=1:
               del self.species_types[species]
               flag=1
        except:
            pass
        if flag==0:    
           try:
               self.species_types[species]-=1
           except:
               pass
               
               
               
# PROBLEM 2 : Meet the Adopter
class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        # Your Code Here
        self.name=name
        self.desired_species=desired_species
    def get_name(self):
        # Your Code Here 
        return self.name
    def get_desired_species(self):
        # Your Code Here
        return self.desired_species
    def get_score(self, adoption_center):
        # Your Code Here
        d=adoption_center.get_species_count()
        try:
           return float(d[self.desired_species])
        except:
           return 0.0
           
           
# PROBLEM 3 : he Flexible and Fearful Adopters
class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, considered_species):
        self.name=name
        self.desired_species=desired_species
        self.considered_species=considered_species
    def get_score(self,adoption_center):
        d=adoption_center.get_species_count()
        s=0.0
        for i in self.considered_species:
          try:
           s=s+d[i]
          except:
           #s=s+0.0
           pass
        if Adopter.get_score(self,adoption_center)+(.3*float(s))>0:
           return Adopter.get_score(self,adoption_center)+(.3*float(s))
        else:
           return 0.0
        
class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, feared_species):
        self.name=name
        self.desired_species=desired_species
        self.feared_species=feared_species
    def get_score(self,adoption_center):
        d=adoption_center.get_species_count()
        s=0.0
        #for i in self.feared_species:
        try:
         s=d[self.feared_species]
        except:
           #s=s+0.0
         pass
        if Adopter.get_score(self,adoption_center)>(.3*float(s)):
           return Adopter.get_score(self,adoption_center)-(.3*float(s))
        else:
           return 0.0
           
           
           
# PROBLEM 4 : AllergicAdopter and MedicatedAllergicAdopter
class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        self.name=name
        self.desired_species=desired_species
        self.allegric_species=allergic_species
    def get_score(self,adoption_center):
        flag=0
        d=adoption_center.get_species_count()
        for i in self.allegric_species:
            if i in d:
                flag=1
                break
        if flag==1:
            return 0.0
        else:
            return Adopter.get_score(self,adoption_center)
class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        self.name=name
        self.desired_species=desired_species
        self.allergic_species=allergic_species
        self.medicine_effectiveness=medicine_effectiveness
    def get_score(self,adoption_center):
        mi=1.0
        d=adoption_center.get_species_count()
        for i in self.allergic_species:
            if i in d:
                if mi>self.medicine_effectiveness[i]:
                    mi=self.medicine_effectiveness[i]
        return Adopter.get_score(self,adoption_center)*mi
        
        
        
# PROBLEM 5 :  The Sluggish Adopter
class SluggishAdopter(Adopter):
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self,name,desired_species)
        self.name = name
        self.desired_species = desired_species
        self.location = (float(location[0]),float(location[1]))
 
    def get_linear_distance(self,to_location):
        x1 = self.location[0]
        y1 = self.location[1]
        x2 = float(to_location[0])
        y2 = float(to_location[1])
        d = ((x1-x2)**2+(y1-y2)**2)**(1.0/2.0)
        return d
    def get_score(self,adoption_center):
        d = self.get_linear_distance(adoption_center.get_location())
        if d < 1.0:
            return adoption_center.get_number_of_species(self.desired_species)
        elif d >= 1.0 and d < 3.0:
            return random.uniform(0.7,0.9)*adoption_center.get_number_of_species(self.desired_species)
        elif d >= 3.0 and d < 5.0:
            return random.uniform(0.5,0.7)*adoption_center.get_number_of_species(self.desired_species)
        elif d >= 5.0:
            return random.uniform(0.1,0.5)*adoption_center.get_number_of_species(self.desired_species)
