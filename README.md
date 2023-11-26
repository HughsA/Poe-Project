# Poe-Project
Edgar Allan Poe Poetry Website. Allows user to choose a poem title by clicking in list or typing and using submit button. Poem title will be sent via HTTP request to a microservice 
that will utilize a json file containing contents of the poems to return chosen poem's content via an HTTP response.

# Food Microservice
Microservice uses Flask to achieve the request, data retrieval, and response. 

You can request data from the microservice by using an HTTP GET request which will need a query parameter which should be the name of the food.
Example for the request using python:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the example URL for the microservice implemented locally
endpoint: "http://127.0.0.1:5000/food_search"

# Substitute "Kiwi" with whatever desired food is
query_param = {"food" : "Kiwi"}
making the new endpoint: "http://127.0.0.1:5000/food_search?food=Kiwi

# Request
HTTP_response = requests.get(url, query_param=query_param)

return HTTP_response.json())
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Data will be returned in a json format. If food is not found, error message containing "food not found" will be returned. If found, json response will contain fat, protein, and carbs of food.

UML Sequence Diagram:

![Assignment9](https://github.com/HughsA/Poe-Project/assets/114530755/c7fe9066-7e64-4f66-a49d-ac33561068ff)



