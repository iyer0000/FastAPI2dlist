# FastAPI2dlist
pip install -r requirements.txt

# To start the application
uvicorn main:app --reload

# To test the docs part of the parameters
http://127.0.0.1:8000/docs#

http://127.0.0.1:8000/docs#/default/addIntegerlist_addlist_post

# For unit test the functionality
python test_sumelements.py

# sample output of the test
.........
----------------------------------------------------------------------
Ran 9 tests in 1.633s
