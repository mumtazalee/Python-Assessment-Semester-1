courses = {}
courses["institution"] = 'UCEN'
courses["city"] = 'Manchester'
courses["locations"] =  'CCM'
# adding a list as a property of courses
courses["course list"] = []


courses["course list"].append("BSc in Designing")
courses["course list"].append("BSc in Networking")
courses["course list"].append("BSc in Software Development")
courses["course list"].append("FDSc in Cyber Security")
courses["course list"].append("BSc in Social Science")


courses['course list'][2] = "BSc in Software Developent"

print(courses)
print(courses['institution'], courses['city'], courses['locations'])
for course in courses['course list']:
    print(courses['institution'], 'has a course called', course)

{
    'institution': 'UCEN',
    'location': 'Manchester',
    'course list': [
        "Bsc in Designing",
        "BSc in Networking",
        "BSc in Software Development",
        "FDSc in Cyber Security",
        "BSc in Social Science"
        ]
}



