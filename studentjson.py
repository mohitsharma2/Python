"""
Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
"""


import json
{
	"details": {
		"Faculty1": {
			"First Name": "Om prakash",
			"Last Name": "Sharma",
			"Photo": " http://tineye.com/images/op.jpg.",
			"Department": "Computer department",
			"Research Areas": "Deep Learning",
			"Contact Detail": [{
				"Phone Number": "9885215654",
				"Email id": "omprakash@gmail.com"
			}]
		},
		"Faculty2": {
			"First Name": "Suraj",
			"Last Name": "Sharma",
			"Photo": " http://tineye.com/images/suraj.jpg.",
			"Department": "Electrical department",
			"Research Areas": "Inductance",
			"Contact Detail": [{
				"Phone Number": "9785255654",
				"Email id": "suraj12@gmail.com"
			}]

		}
	}
}
print(type())

or==================or=====================================

[{
	"Faculty1": [{
		"First Name": "Om prakash",
		"Last Name": "Sharma",
		"Photo": " http://tineye.com/images/op.jpg.",
		"Department": "Computer department",
		"Research Areas": "Deep Learning",
		"Contact Detail": [{
			"Phone Number": "9885215654",
			"Email id": "omprakash@gmail.com"
		}]
	}]
}, {
	"Faculty2": [{
		"First Name": "Suraj",
		"Last Name": "Sharma",
		"Photo": " http://tineye.com/images/suraj.jpg.",
		"Department": "Electrical department",
		"Research Areas": "Inductance",
		"Contact Detail": [{
			"Phone Number": "9785255654",
			"Email id": "suraj12@gmail.com"
		}]

	}]
}]
