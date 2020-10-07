# Coffee Shop Full Stack

 Originally this was a project of the Full stack nano degree offered by udacity. It's a simple Coffee shop single web app using ionic/angular as the frontend framework, Flask and sqlight, sqlalchemy, postgresql as the backend.

### Udacity : https://udacity.com/. 

The application can:

1) Display graphics representing the ratios of ingredients in each drink.
2) Allow public users to view drink names and graphics.
3) Allow the shop baristas to see the recipe information.
4) Allow the shop managers to create new drinks and edit existing drinks.

# To start the app "Required dependancies", Kindly refer back to both README files mentioned below.

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

# Api Info ;) 

Based on: REST principles! each endpoint returns a JSON metadata.
Base Uri: "Your_local_Host:Port/". 
ex: http://localhost:5000 "Server
ex: http://localhost:8100 "ionic" 

## Allowed HTTP methods "For now":-
GET:	Retrieves resources
Post:	Creates resources
Patch:	Updates resources
DELETE:	Deletes resources

### EndPoints:-

GET '/drinks' "Public"
GET '/drinks-detail' "Requires AUTH"
POST '/drink' "Requires AUTH"
PATCH '/drink/id' Note: id has to be an int, "Requires AUTH"
DELETE '/drink/id' Note: id has to be an int, "Requires AUTH"

### I'll continue to work on this project to add more featuers later on.
