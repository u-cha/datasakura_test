# This is a test assignment for Datasakura

This API leverages FastAPI to provide an endpoint to calculate GameResultOutput  
as defined by the assignment.

To run the project you'll need to `git clone` it from this repo,
then install the dependencies with `poetry install --no-root` (if you don't have  
Poetry install please proceed to its official site for instructions).

I suggest that you also run `poetry shell` after deps installation to make sure that  
you are working inside a safe virtual envrionment

You may decide to run `uvicorn main:app --reload`, if you wish to see the API running.
You can then check it on `localhost:8000/docs`.

# Endpoint
This API has the only endpoint which takes `GameResultInput` as input and  
return `GameResultOuput` after processing the game results on backend.

Pydantic model safeguards the endpoint so that only valid data can be taken in.

The endpoint uses POST method, so the data should be sent via request body.

# Service
Backend will use a service to determine the game results.
I decided to process the board for each player through `PlayerPosition` class. It  
could be helpful if we decided to update player position while the game is running  
by providing an updated board through `.update(<board>)` method. It is not used now,  
I just want to justify this choice.  

There is also a note on how the result is calculated:
- it is assumed that start_position integers are defined as 0 and 23 for the opponents 
(although it is not validated by the model now)


# Testing
I decided to add some unit testing for the service to make sure that at least  
some of the cases are tested.
You can run `pytest` to check that the service works.

NB! I understand that test code could be improved in terms of how the code is organised.
I am also sure that not all cases are properly tested, the idea was to check only the main scenarios  
as defined in the assignment.