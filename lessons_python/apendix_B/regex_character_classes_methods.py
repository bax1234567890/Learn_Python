import re

from sqlalchemy import true

# search() - find first match inside the string
# findall() - find all matches inside the string

# Find just first match
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex
resume = """	Enhanced product 323-456-3245 reliability through API testing using Postman and Swagger.
	Developed daily Gherkin test cases, integrated with CI/CD in Azure DevOps.
	Analyzed automation reports in regression testing and conducted integration testing, ensuring system-wide compatibility.
	Implemented Regression and Integration 345-654-7890 testing strategies. Applied Risk-Based Testing for prioritizing test scenarios and conducted Exploratory Testing. 
	Participated in Scrum ceremonies: Daily Stand-Ups, Sprint Planning, Backlog Grooming, Sprint Retrospectives, Release Planning, and Demo presentations to showcase new features and progress.
	Managed and executed queries in AWS, ensuring 345-435-2345 optimal """
search = phoneRegex.search(resume) # find first
print(search)


# Find all matches
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex
resume = """	Enhanced product 323-456-3245 reliability through API testing using Postman and Swagger.
	Developed daily Gherkin test cases, integrated with CI/CD in Azure DevOps.
	Analyzed automation reports in regression testing and conducted integration testing, ensuring system-wide compatibility.
	Implemented Regression and Integration 345-654-7890 testing strategies. Applied Risk-Based Testing for prioritizing test scenarios and conducted Exploratory Testing. 
	Participated in Scrum ceremonies: Daily Stand-Ups, Sprint Planning, Backlog Grooming, Sprint Retrospectives, Release Planning, and Demo presentations to showcase new features and progress.
	Managed and executed queries in AWS, ensuring 345-435-2345 optimal """
search = phoneRegex.findall(resume) # find all
print(search)


# To or more groups with Find All Matches
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
search2 = phoneRegex.findall(resume) # find all
print(search2)


lyrics = ('12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, 7 swans a-swimming, 6 geese a-laying, 5 golden rings, 4 golden rings, 3 French hens, 2 turtle doves, 1 partridge in a pear tree.')
xmasRegex = re.compile(r'\d+\s\w+') # diget, space, word, if next is not word stop finding
find = xmasRegex.findall(lyrics)
print(find)


# Find particular characters in string
vowelRegex = re.compile(r'[aeiouAEIOU]')
find = vowelRegex.findall('Robocop eats baby food.')
print(find)

# Find double characters in string
vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
doublefind = vowelRegex.findall('Robocop eats baby food.')
print(doublefind)

# Match everything is not specified
vowelRegex = re.compile(r'[^aeiouAEIOU]') # "^"
find = vowelRegex.findall('Robocop eats baby food.')
print(find)

# find one or more words (\w+)
namesRegex = re.compile(r'Agent \w+') # one or more characters
agents = namesRegex.findall('Agent Skally asked Agent Malder')
print(agents)

# find and substitute - anytime find word substitute it with another
namesRegex = re.compile(r'Agent \w+') # one or more characters
agents_redacted = namesRegex.sub('REDACTED', 'Agent Skally asked Agent Malder') # substitute a word with another
print(agents_redacted)

# Substitute full name with 1 character
namesRegex = re.compile(r'Agent (\w)\w*') # Group 1 - (\w); Group 2 - \w*
agents_short = namesRegex.sub(r'Agent \1*****', 'Agent Skally asked Agent Malder') # substitute a word with another
print(agents_short)


def test_multiply(x, y):
    result = 0
    for i in range(y):  # Corrected loop condition
        result += x
    return result  # Returns the multiplication result
