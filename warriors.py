class Team:
   def __init__(self, name, city, conference, record=None):
      self.name = name
      self.city = city
      self.conference = conference 
      self.record = record

   def __str__(self):
      result = (
         f"Team: {self.name}\n"
         f"City: {self.city}\n"
         f"Conference: {self.conference}\n"
         f"Record: {self.record}\n"
      )
      return result
   # getters
   @property
   def name(self):
      return self.__name
   
   @property
   def city(self):
      return self.__city 
   
   @property 
   def conference(self):
      return self.__conference 
   
   @property 
   def record(self):
      return self.__record
   
   # setters
   @name.setter
   def name(self, name):
      if len(name) > 10 or " " in name:
         raise ValueError("Invalid naming convention detected")
      
      self.__name = name

   @city.setter
   def city(self, city):
      if len(city) > 50:
         raise ValueError("Invalid naming convention detected")
      
      self.__city = city

   @conference.setter
   def conference(self, conference):
      if conference not in ["Eastern", "Western"]:
         raise ValueError("Invalid conference selection")
      
      self.__conference = conference 

   @record.setter 
   def record(self, record = None):
      if record is None:
         self.__record = {"Wins": 0, "Losses": 0}

      else:
         self.__record = record

   # compare winning percentage vs another nba team
   def compare_records(self, team):
      opponent_wins = team.record.get("Wins")
      opponent_losses = team.record.get("Losses")
      opponent_winning_pct = opponent_wins / (opponent_wins + opponent_losses)

      team_wins = self.record.get("Wins")
      team_losses = self.record.get("Losses")
      team_winning_pct = team_wins / (team_wins + team_losses)

      return team_winning_pct, opponent_winning_pct
   
   # print stats of head to head matchup 
   def print_matchup(self, team):
      team_pct, opponent_pct = self.compare_records(team)

      result = f"{team.name} winning pct: {opponent_pct * 100:.0f}%"
      result1 = f"{self.name} winning pct: {team_pct * 100:.0f}%"
      
      return result, result1


record = {"Wins": 14, "Losses": 0}
record2 = {"Wins": 11, "Losses": 7}
warriors = Team("Warriors", "San Francisco", "Western", record)
bulls = Team("Bulls", "Chicago", "Eastern", record2)

warriors_win_pct, bulls_win_pct = warriors.print_matchup(bulls)
# print(warriors_win_pct)
# print(bulls_win_pct)

"""
class BaseClass:
   def __init__(self, identifier):
      self.identifier = identifier

   def message(self):
      print("Welcome to the Base Class")
      print(self.identifier)

   def message_base_class(self):
      print("This is a message from the base class")
      print(self.identifier)

class ChildClass:
   def __init__(self, identifier):
      BaseClass.__init__(self, identifier)

   def message(self):
      print("Welcome to the ChildClass")
      print("This is inherited from the BaseClass?")
      print(self.identifier)
      

base_obj = BaseClass("base")
base_obj.message()

child_obj = ChildClass("child")
child_obj.message()
child_obj.message_base_class()
"""

class BaseClass:
   def __init__(self, property):
      self.property = property
   
   def message(self):
      print("Welcome to the BaseClass!!")

   def message_base_class(self):
      print("This is a message from BaseClass")

class ChildClass(BaseClass):
   def __init__(self, property):
      BaseClass.__init__(self, property)

   def message(self):
      print("Welcome to ChildClass")
      print("This is inherited from BaseClass")

base_obj = BaseClass("base")
base_obj.message()

child_obj = ChildClass("child")
child_obj.message()
child_obj.message_base_class()