# This is a test assignment for Datasakura

This API leverages FastAPI to provide an endpoint to calculate GameResultOutput  
as defined by the assignment.

To run the project you'll need to `git clone` it from this repo,
then install the dependencies with `poetry install --no-root` (if you don't have  
Poetry install please proceed to its official site for instructions).

I suggest that you also run `poetry shell` after deps installation to make sure that  
you are working inside a safe virtual envrionment

# Endpoint
This API has the only endpoint which takes `GameResultInput` as input and  
return `GameResultOuput` after processing the game results on backend.

Pydantic model safeguards the endpoint so that only valid data can be taken in.

The endpoint uses POST method, so the data should be sent via request body.

# Testing
I decided to add some unit testing for the service to make sure that at least  
some of the cases are tested.
You can run `pytest` to check that the service works.

NB! I understand that test code could be improved in terms of how the code is organised.
I am also sure that not all cases are properly tested, the idea was to check only the main scenarios  
as defined in the assignment.