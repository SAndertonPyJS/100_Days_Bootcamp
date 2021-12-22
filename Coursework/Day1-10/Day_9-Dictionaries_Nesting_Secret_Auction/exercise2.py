#Here is the travel log as given to us by the exercise, we are to add another
#place or places to it using dictionaries
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

# first we create a new function called add_new_country and feed in our arguments:
#Arguments being the country, amount of visits and the cities in particular
def add_new_country(country_visited, times_visited, cities_visited):
  #next because in effect travel log is a list of dictionaries, we want to create a new dictionary we can add to:
  new_country = {}
  #after this we then feed in the information:
  new_country["country"] = country_visited
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  #finally as stated travel log is a list, we append it with the new dictionary:
  travel_log.append(new_country)

#now we run our function:
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#and print!
print(travel_log)



