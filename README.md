Flash cards application


Added skeleton code for BE
Added skeleton code for FE


Time used -> prob 8 hours 30 mins
Time left -> 0 


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

    

    a. If the answer is wrong and current wrong choices count is 9 -> Added the card to hidden 
    b. If the answer is wrong but current wrong choices count is < 9 -> Moved the card to bin 1 (current_stage ) , incremented wrong_choices by 1 and set the up_in time to current_time + 5 seconds ( as it is in bin 1)
    c. If the answer is right and current bin is 10 -> Added the card to hidden 
    d. If the answer is right and current bin < 10  -> Moved the card to current_bin + 1 , up_in time increased 

4. Added get card/cards for admin -> This essentially is 2 apis
    a. Get details of 1 single card if card_id is provided
    b. Get all cards if the card_id is missing

5. Get successfully cards for admin  ->  We are fetching all the cards where current_stage = 11 and hidden is true (i.e) all the stages has been passed

6.Get failed cards for admin  ->  We are fetching all the cards where wrong_choices = 10

7. Added reset api for admin -> This is essentially 2 apis
    a. If a card_id is passed, That particular card is set to bin 0 , all wrong choices are removed and it is shown to the user

        The idea for the above api is, since we are not allowing the user to add a card with the same key and desc and the user wants to re-review or revise, as an admin we can reset that card so that user can learn it again.
    
    b. reset all cards - > Essentially does the above but for all cards in the database

8. Update card desc -> allowing this as of now just for admin


Other than these there were couple more which I did implement:
a. A variety of checks for data
b. error and general responses ( more of error catching and returning the errors if they arise )

Things I still need to do:
1. Refactor the code ( its a maybe and under low prior)
2. Added 2 or 3 more checks to return "you are temp done" and "completely done" under get ( complete )
3. Merge the psql and backend into the same docker file.
4. Test and bug fix the code ( majority of it is done )
5. Prevent incoming request to jump states 
    Right now if the incoming state update is to 2 and in the next request I pass 9 , it goes through but it should not be the case. From 2 it needs to go to 3 ( This is complete )
6. A issue only when sending requests from BE, If we keep sending the card updates for success or failure even after the thershold is hit ( 11 for stage and 10  for wrong , they keep updating ) ( complete )


Improvements:
1. I had created 4 seperate views , 1 for user and 3 for admin which is not at all required.. Since I was using Methodview I wanted to continue with that and not switch to ViewSets which can handle multiple gets under the same view as well as define seperate router endpoints to them


What would I change if more time given:
1. Change the views from MethodView into Viewsets and add specific routes for the same.
2. I felt like I have a lot of queries which infact I can reduce it by making them dynamic based on the a couple of parameters but I did not want to take that route yet.. Just wanted to get a rough draft done before I do optimizations.
3. I could have split the admin urls and views out from generic cards thus creating a new handler for easier code readibility and maintainablity but didnt as I wanted to finish the draft first in the given time frame.
4. I need to get back and add comments , there are couple of places where comments are required!


React side:
Gotta Agree, not my cup of tea yet, did a small course and started working on this and i know i still have a very long way!

Stuff implemented:
1. Create card
2. Get card
3. Edge cases and their responses [ no cards , perma done and stuff]
4. Admin lvl apis for fetch all cards
5. Reset all cards
6. Completed Cards ( either with wrong answers -> 10 or state 11)
7. Learnt cards -> state 11
8. Admin Fetch 1 card

Issues:
1. Clicking on fetch of admin cards is not hiding the previous ones, but appending to the data table ( prob has something to do with reusing the data table maybe)
2. The errors are not caught / used 
3. This is just a rough piece which i did with couple of hours in react refresh after almost a year away so there will be sub par implementation and bugs !

Deployments:
Deployed into AWS ec2 instances

Common commands ran for both FE and BE Ec2 instance deployments:
1. yum install docker
2. yum install git
3. git config --global user.name ""
4. git config --global user.email ""
5. service docker start 
6. usermod -a -G docker ec2-user 
7. sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
8. git clone https://github.com/Yalamarthi97/hiring-sriharsha-y-flashcards.git


After cloning 

For deploying BE:
1. cd into rest_api
2. docker-compose -f psql_docker-compomse,yml up -d
3. docker-compose -f docker-compomse,yml build
4. docker-compose -f docker-compomse,yml up -d

For Deploying FE:
1. cd into flash-cards
2. update apiConnection.tsx under utils to point to BE deployed url
3. docker-compose -f docker-compose build
4. docker-compose -f docker-compose up 


Networking Added:
psql port  at 5432
backend rest api at port 5555
frontend port at 3000

For running in local:
1. run psql_docker-compose
2. Update .env under backend folder to point to psql port and endpoint -> host.docker.internal
3. run docker-compose for be
4. update apiConnection.tsx to host.docker.internal along with port of 5556 / 5555 based on BE docker-compose
5. run docker-compomse up of FE


Deployments Folder is just for references!!

