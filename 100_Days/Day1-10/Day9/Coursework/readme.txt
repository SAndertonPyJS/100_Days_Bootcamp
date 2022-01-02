### --- CURRENT COURSEWORK --- ###

Learning basics about dictionaries and nesting

### --- GOALS --- ###

To be able to use dictionaries and nested functions to create more complex programs

### --- EXERCISES --- ###


1 - Student Scores // looping through dictionaries
	
	Create a piece of code that will loop through a dictionary to find the highest score in
    the dict and then assign the name associated with it a grade in a second dict

    example:
    {
    Harry: 81,
    Hermione: 99
    }

    output:

    {
    "Harry": "Exceeds Expectations",
    "Hermione": "Outstanding",
    }


2 - Travel Log // dictionaries in lists

    For this exercise we are to create a function that will allow new countries to be added to
    the dict

    ex:

    travel_log = [
        {
            "country": "France",
            "visits": 12,
            "cities": ["Paris", "Lille", "Dijon"]
        },

        {
            "country": "Germany",
            "visits": 5,
            "cities": ["Berlin", "Hamburg", "Stuttgart"]
        },
                ]

    add That you have been to russia, twice, visiting moscow and saint petersburg

    output:
        [
            {'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, 
            {'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']}, 
            {'country': 'Russia', 'visits': 2, 'cities': ['Moscow', 'Saint Petersburg']},
        ]