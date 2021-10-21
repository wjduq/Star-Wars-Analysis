import re 

newHopePattern = r"(\b[A-Z ']+\b)\n\s+(.*(?:\n\s+.*)*)\n\n"

newHopeScript = open('Star-Wars-A-New-Hope.txt', 'r')

matches = re.findall(newHopePattern, newHopeScript.read())
print(matches)

newHopeScript.read()