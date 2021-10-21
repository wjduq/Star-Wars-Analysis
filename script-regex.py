import re 

newHopePattern = r"(\b[A-Z ']+\b)\n[^\n]+[A-Z(]"

newHopeScript = open('Star-Wars-A-New-Hope.txt', 'r')

matches = re.findall(newHopePattern, newHopeScript.read())
print(matches)
