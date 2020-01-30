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

jso="""
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
 """
my=json.loads(jso)
print(my)
type(my)
me=json.dumps(my)
print(me)
type(me)
with open("C:/Users/mohit/Desktop/studennn.json", "w") as write_file:
    json.dump(jso, write_file)

with open("C:/Users/mohit/Desktop/studennn.json", "r") as read_file:
    j=json.load(read_file)
    print(j)
 
"""
output===================================================================


my=json.loads(jso)

print(my)
{'details': {'Faculty1': {'First Name': 'Om prakash', 'Last Name': 'Sharma', 'Photo': ' http://tineye.com/images/op.jpg.', 'Department': 'Computer department', 'Research Areas': 'Deep Learning', 'Contact Detail': [{'Phone Number': '9885215654', 'Email id': 'omprakash@gmail.com'}]}, 'Faculty2': {'First Name': 'Suraj', 'Last Name': 'Sharma', 'Photo': ' http://tineye.com/images/suraj.jpg.', 'Department': 'Electrical department', 'Research Areas': 'Inductance', 'Contact Detail': [{'Phone Number': '9785255654', 'Email id': 'suraj12@gmail.com'}]}}}

me=json.dumps(my)

print(me)
{"details": {"Faculty1": {"First Name": "Om prakash", "Last Name": "Sharma", "Photo": " http://tineye.com/images/op.jpg.", "Department": "Computer department", "Research Areas": "Deep Learning", "Contact Detail": [{"Phone Number": "9885215654", "Email id": "omprakash@gmail.com"}]}, "Faculty2": {"First Name": "Suraj", "Last Name": "Sharma", "Photo": " http://tineye.com/images/suraj.jpg.", "Department": "Electrical department", "Research Areas": "Inductance", "Contact Detail": [{"Phone Number": "9785255654", "Email id": "suraj12@gmail.com"}]}}}

my=json.loads(jso)
print(my)
type(my)
me=json.dumps(my)
print(me)
type(me)
{'details': {'Faculty1': {'First Name': 'Om prakash', 'Last Name': 'Sharma', 'Photo': ' http://tineye.com/images/op.jpg.', 'Department': 'Computer department', 'Research Areas': 'Deep Learning', 'Contact Detail': [{'Phone Number': '9885215654', 'Email id': 'omprakash@gmail.com'}]}, 'Faculty2': {'First Name': 'Suraj', 'Last Name': 'Sharma', 'Photo': ' http://tineye.com/images/suraj.jpg.', 'Department': 'Electrical department', 'Research Areas': 'Inductance', 'Contact Detail': [{'Phone Number': '9785255654', 'Email id': 'suraj12@gmail.com'}]}}}
{"details": {"Faculty1": {"First Name": "Om prakash", "Last Name": "Sharma", "Photo": " http://tineye.com/images/op.jpg.", "Department": "Computer department", "Research Areas": "Deep Learning", "Contact Detail": [{"Phone Number": "9885215654", "Email id": "omprakash@gmail.com"}]}, "Faculty2": {"First Name": "Suraj", "Last Name": "Sharma", "Photo": " http://tineye.com/images/suraj.jpg.", "Department": "Electrical department", "Research Areas": "Inductance", "Contact Detail": [{"Phone Number": "9785255654", "Email id": "suraj12@gmail.com"}]}}}
Out[27]: str

type(my)
Out[28]: dict

with open("C:/Users/mohit/Desktop/studennn.json", "w") as write_file:
    json.dump(jso, write_file)

with open("C:/Users/mohit/Desktop/studennn.json", "w") as write_file:
    json.dump(jso, write_file)

with open("C:/Users/mohit/Desktop/studennn.json", "r") as read_file:
    jso=json.load(read_file)
    print(my)
{'details': {'Faculty1': {'First Name': 'Om prakash', 'Last Name': 'Sharma', 'Photo': ' http://tineye.com/images/op.jpg.', 'Department': 'Computer department', 'Research Areas': 'Deep Learning', 'Contact Detail': [{'Phone Number': '9885215654', 'Email id': 'omprakash@gmail.com'}]}, 'Faculty2': {'First Name': 'Suraj', 'Last Name': 'Sharma', 'Photo': ' http://tineye.com/images/suraj.jpg.', 'Department': 'Electrical department', 'Research Areas': 'Inductance', 'Contact Detail': [{'Phone Number': '9785255654', 'Email id': 'suraj12@gmail.com'}]}}}

with open("C:/Users/mohit/Desktop/studennn.json", "r") as read_file:
    jso=json.load(read_file)
    print(me)
{"details": {"Faculty1": {"First Name": "Om prakash", "Last Name": "Sharma", "Photo": " http://tineye.com/images/op.jpg.", "Department": "Computer department", "Research Areas": "Deep Learning", "Contact Detail": [{"Phone Number": "9885215654", "Email id": "omprakash@gmail.com"}]}, "Faculty2": {"First Name": "Suraj", "Last Name": "Sharma", "Photo": " http://tineye.com/images/suraj.jpg.", "Department": "Electrical department", "Research Areas": "Inductance", "Contact Detail": [{"Phone Number": "9785255654", "Email id": "suraj12@gmail.com"}]}}}

with open("C:/Users/mohit/Desktop/studennn.json", "r") as read_file:
    j=json.load(read_file)
    print(j)

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
 

my=json.loads(jso)
print(my)
type(my)
me=json.dumps(my)
print(me)
type(me)
with open("C:/Users/mohit/Desktop/studennn.json", "w") as write_file:
    json.dump(jso, write_file)


with open("C:/Users/mohit/Desktop/studennn.json", "r") as read_file:
    j=json.load(read_file)
    print(j)
{'details': {'Faculty1': {'First Name': 'Om prakash', 'Last Name': 'Sharma', 'Photo': ' http://tineye.com/images/op.jpg.', 'Department': 'Computer department', 'Research Areas': 'Deep Learning', 'Contact Detail': [{'Phone Number': '9885215654', 'Email id': 'omprakash@gmail.com'}]}, 'Faculty2': {'First Name': 'Suraj', 'Last Name': 'Sharma', 'Photo': ' http://tineye.com/images/suraj.jpg.', 'Department': 'Electrical department', 'Research Areas': 'Inductance', 'Contact Detail': [{'Phone Number': '9785255654', 'Email id': 'suraj12@gmail.com'}]}}}
{"details": {"Faculty1": {"First Name": "Om prakash", "Last Name": "Sharma", "Photo": " http://tineye.com/images/op.jpg.", "Department": "Computer department", "Research Areas": "Deep Learning", "Contact Detail": [{"Phone Number": "9885215654", "Email id": "omprakash@gmail.com"}]}, "Faculty2": {"First Name": "Suraj", "Last Name": "Sharma", "Photo": " http://tineye.com/images/suraj.jpg.", "Department": "Electrical department", "Research Areas": "Inductance", "Contact Detail": [{"Phone Number": "9785255654", "Email id": "suraj12@gmail.com"}]}}}

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
"""


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
            
            
            
            
            
{
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
		"Contact Detail": {
			"Phone Number": "9785255654",
			"Email id": "suraj12@gmail.com"
		}

	}
}










