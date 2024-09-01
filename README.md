Chattr is a free online platform for chatting about anything you love! Users can create a account and use it to chat with other users. The app has multiple topics, each having one chat, making the experience feel like you're chatting with friends.

Chattr includes following features:



!!BECAUSE OF FLY.IO WEBSITE BEING DOWN ON 1.9. THE PROJECT CAN ONLY BE TESTED LOCALLY. INSTRUCTIONS IN THE END OF README!!



-Multiple chats (topics), that can be added and modified by admins.
-Users  that have signed in can send and read messages in the chats.
-Users can create an account and sign in using a password.
~~-Users can add a profile picture.~~
-Users can have a admin status, that gives the moderator abilities (removing messages, ~~accounts~~, etc.)
~~-There is a search function. Users can search for messages containing a spesific word.~~
-Users can give likes to messages.



1.9. UPDATE:

    - Some features missing because of lack of time.
    - Users can only get admin rights through psql cmd
    - Admin users can remove messages and create new topics
    - Users can give a like and remove a like
    - 

18.8. UPDATE:

    - Login, registration, sending messages and navigation are done.
    - The appearance has been updated using Bootstrap

    TODO:
    - Update the appearance
    - Password suitability check
    - Add admin features
    - Make the messages appear in the right order
    - Add likes and favourited topics
    - Add profile pictures
    - Add search function


4.8. UPDATE:

    - The application can't be run or tested yet because of problem with SQLAlchemy. I've been trying to write as many functions as I can without trying the app.
    - I hope I'll get the SQLalchemy problem fixed soon with some help so I can actually start developing the app.
    - Some of the basic functions such as login, getting the topics and the messages are somewhat done.
    - Basic structure of the project is clear.

INSTRUCTIONS FOR TRYING THE PROJECT:

1. Clone this repository from github

2. Create a virtual environment into the folder using:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install the requirements with:
```
pip install < requirements.txt
```

4. Create a file ".env" and set the environmental variables:
```
DATABASE_URL=
SECRET_KEY=
```

5. Create all the necessary tables by running:
```
psql < schema.sql
```

6. Add data to the database for testing:
```
psql < testdata.sql
```
This will add some topics and a admin account:
name: adminuser1234
password: 12345678

More topics can be created using the admin account.

7. Now run the project with:
```
flask run
```
