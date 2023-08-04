# hiring-sriharsha-y-flashcards

Added skeleton code for BE
Added skeleton code for FE


Time used -> 3 hours 50 or almost 4 hours 
Time left -> around 2 


for now checking only under cards table but need to check under forgotten cards as well as we should not create the card with same value and desc if it is forgotten or already present

Set time limit for myself -> 7 hours 

Hour 1 + 20 mins:  Time left approx -> 5 hours 40 mins

1. Looked into the logic on how I can achieve the card one after the other
2. Created the DB
3. Added psql driver and some decorators for it
4. Created 2 docker-compose files , one for psql and other for backend
5. Added cards view and url
6. Troubelshooting on why flask was not restarting
7. Worked on creating the tables into the psql instance and storing the data
8. Updated requirements.txt 
9. Tried connecting to psql through docker ( I kinda was left searching for some answers on the internet)
10. Iterated over various ways on how  I can acheive this project

Spent 25 mins, looking into the schema for the db , altering the existing one and trying to create queries
Combined both the tables into 1 as I felt having 2 seperate right now might not be required.

Time spent in this session.. complete is almost 2 hours 30 mins + or  - 15 mins
I felt like I did a big chunk of backend apis in this session..
There are a couple of standouts right now which I shall add in the bottom under improvements and why I did this way:

Session highlights:
1. Implemented the get card function
    a. If there is a card under the conditions it is ready or there is a card in bucket 0 , I send the card out
    b. If there is no data , return there is no data
2. Added create card where
    a. If the card is already present ( forgotten or still in the bucket .. both the cases), am not allowing to create the card.
    b. If the card is not present -> create the card
3. Added Update method -> This essentially holds the logic of the flash cards app

    -> Before going into the implementations.. the hidden value on the db is present to divide the cards between the ones to be shown to the user and not shown

    -> Answered boolean is added so that if the card was added into hidden because of wrong answering the answered is false , if the card is added because of completing all the bins answered is true.
    

    a. If the answer is wrong and current wrong choices count is 9 -> Added the card to hidden (answered -> False ) 
    b. If the answer is wrong but current wrong choices count is < 9 -> Moved the card to bin 1 (current_stage ) , incremented wrong_choices by 1 and set the up_in time to current_time + 5 seconds ( as it is in bin 1)
    c. If the answer is right and current bin is 10 -> Added the card to hidden ( answered -> True )
    d. If the answer is right and current bin < 10  -> Moved the card to current_bin + 1 , up_in time increased 

4. Added get card/cards for admin -> This essentially is 2 apis
    a. Get details of 1 single card if card_id is provided
    b. Get all cards if the card_id is missing

5. Get successfully cards for admin  ->  This is where the answered is being used where we are fetching all the cards where answered is true (i.e) all the stages has been passed

6.Get failed cards for admin  ->  This is where the answered is being used where we are fetching all the cards where answered is false (i.e) number of wrong choices is 10

7. Added reset api for admin -> This is essentially 2 apis
    a. If a card_id is passed, That particular card is set to bin 0 , all wrong choices are removed and it is shown to the user

        The idea for the above api is, since we are not allowing the user to add a card with the same key and desc and the user wants to re-review or revise, as an admin we can reset that card so that user can learn it again.
    
    b. reset all cards - > Essentially does the above but for all cards in the database


Other than these there were couple more which I did implement:
a. A variety of checks for data
b. error and general responses ( more of error catching and returning the errors if they arise )

Things I still need to do:
1. Refactor the code ( its a maybe and under low prior)
2. Added 2 or 3 more checks to return "you are temp done" and "completely done" under get
3. Merge the psql and backend into the same docker file.


Improvements:
1. I had created 4 seperate views , 1 for user and 3 for admin which is not at all required.. Since I was using Methodview I wanted to continue with that and not switch to ViewSets which can handle multiple gets under the same view as well as define seperate router endpoints to them


What would I change if more time given:
1. Change the views from MethodView into Viewsets and add specific routes for the same.
2. I felt like I have a lot of queries which infact I can reduce it by making them dynamic based on the a couple of parameters but I did not want to take that route yet.. Just wanted to get a rough draft done before I do optimizations.
3. I could have split the admin urls and views out from generic cards thus creating a new handler for easier code readibility and maintainablity but didnt as I wanted to finish the draft first in the given time frame.
4. I need to get back and add comments , there are couple of places where comments are required!
