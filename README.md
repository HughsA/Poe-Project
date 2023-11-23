# Poe-Project
Edgar Allan Poe Poetry Website. Allows user to choose a poem title by clicking in list or typing and using submit button. Poem title will be sent via HTTP request to a microservice 
that will utilize a json file containing contents of the poems to return chosen poem's content via an HTTP response.

Microservice uses Flask to achieve the request, data retrieval, and response. 

You can request data from the microservice by using an HTTP GET request which will need a query parameter which should be the title of the poem.
Example for the request using python:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This should be the URL for the microservice
endpoint: "http://127.0.0.1:5000/poe_search"

# Substitute "Lenore" with whatever desired poem is
query_param = {"title" : "Lenore"}

# Request
HTTP_response = requests.get(url, query_param=query_param

return HTTP_response.json())
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Data will be returned in a json format. If poem is not found, error message containing "poem not found" will be returned. If found, json response will contain contents of poem.
User can insert data into HTML so poem will be displayed on screen.

UML Sequence Diagram:

![Screen Shot 2023-11-22 at 6 23 11 PM](https://github.com/HughsA/Poe-Project/assets/114530755/9e293890-ec3c-464c-a911-23c937d853d9)




