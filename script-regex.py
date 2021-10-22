import re 

newHopePattern = r"(\b[A-Z ']+\b)\n[^\n]+[A-Z(]"
newHopeScript = open('Star-Wars-A-New-Hope.txt', 'r')
newHopeMatches = re.findall(newHopePattern, newHopeScript.read())
print(newHopeMatches)

empireStrikesBackPattern = r"(\b[A-Z ']+\b)\n[^\n]+[A-Z(]"
empireStrikesBackScript = open('Star-Wars-The-Empire-Strikes-Back.txt','r')
empireStrikesBackMatches = re.findall(empireStrikesBackPattern, empireStrikesBackScript.read())
print(empireStrikesBackMatches)

returnOfTheJediPattern = r"\n(\b[A-Z ']{3,}\b)\n"
returnOfTheJediScript = open('Star-Wars-Return-of-the-Jedi.txt','r')
returnOfTheJediMatches = re.findall(returnOfTheJediPattern, returnOfTheJediScript.read())
print(returnOfTheJediMatches)

returnOfTheJediScript.read()

#Test reets
#This is another test