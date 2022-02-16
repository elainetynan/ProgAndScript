# labQ1.py
#
# Data types
#
# Author: Elaine Tynan

# labQ1.py
# data types
# Author: Andrew Beatty

numberOfQuestions = 5 # a. int
averageAge = 23.4 # b. float
debugMode = True # c. boolean
name = "joe" # d. string
ages = [] # e. list/array
months = ('Jan', 'Feb', 'Mar') # f. tulpe   g. string (months[1] = 'Feb')
book = {} # h. dict
stuff = [ 12 , 'Fred', False, {}] # i. list/array   j.  boolean (stuff[2] = False)
someone = dict(firstname = "joe") # k. dict   l. string (someone["firstname"]= "joe")
me = { # m. dict
    "firstName" : "Andrew",
    "teaching" : [{ # n. array (me["teaching"]= array of dicts)
            "courseName" : "programming",
            "semester" : 1 # o. int (me["teaching"][0]["semester"] = 1)
        },{ # p. error in case if corrected, string as me["teaching"][0]["courseName"] = "programming"
            "courseName" : "Data Representation",
            "semester" : 2
        }
    ]
}