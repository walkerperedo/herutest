## General info

This is a test project for heru, it's written with python, FastApi, pyMongo.
This project uses as database mongoDB because it's a small project and mongo gives us more flexibility to manipulate data

## Routes

This project has 4 main routes

# Trip

GET /trip/{tripId} to get a single trip.

GET /trip/user/{userId} to get all the trips for one user.

POST /trip to post a trip.

# User

POST /user to create an user

## How to run this app

I will dockerize this app later so it can run in any other computer.

To run this app you need to install python3 pip3 and pipenv.

Once you have that installed you have to run pipenv shell to create the virtual enviroment for the project.

After that you have to install all the dependecies of the project with pipenv install.

And finally to expose the port you run "uvicorn main:app" this will automatically will expose the port 8000.
