# General info

This is a test project for heru, it's written with python, FastApi, pyMongo.
This project uses as database mongoDB because it's a small project and mongo gives us more flexibility to manipulate data

# Routes

This project has 4 main routes

## Trip

GET /trip/{tripId} to get a single trip.

GET /trip/user/{userId} to get all the trips for one user.

POST /trip to post a trip.

## User

POST /user to create an user

## How to run this app

This app is already dockerized so the you only need docker and docker-compose installed in you computer.

To run this app write this command.

docker-compose build && docker-compose up

This will expose the app in the port 8000
  
