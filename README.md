# Prime_Gen_API

#![PRIME_API(2)](https://user-images.githubusercontent.com/78364361/189113151-aad58f26-6830-42c1-a53a-507c36b47225.gif)


https://user-images.githubusercontent.com/78364361/189113707-7c43f182-89e4-4a41-ac30-208ba59f3b32.mp4



Dependencies:
pip install flask flask-sqlalchemy

STEPS:
1) Make two files with name algo.py and app.py, where algo file contains all algorithms and app file contain flask web framework. Then run these files.
2) Create a test.db file in command prompt/ powershell.
   How to create db file / Queries for CMD:
   i) python
   ii) from app import db                        # whare app.py and test.db should be in same directory. 
   iii) db.create_all()
3) Open any API client like insomnia, postman etc. Write api link in the url.
4) Write all queries in json file and Press "Send" w.r.t "POST". 
5) Now all the API queries will be stored in test.db, to read all the data we are using "SQLite Viewer".
6) Drag and drop the test.db file to SQLite Viewer. Now all the data are readable and editable.


S/W, programming language, web frameworks used:
i) VS code.
ii) Flask web framework, python.
iii) Insomnia API client.
iv) SQLite Viewer.(link-https://inloop.github.io/sqlite-viewer/#)
