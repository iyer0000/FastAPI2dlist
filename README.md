# FastAPI2dlist
pip install -r requirements.txt

# To start the application
uvicorn main:app --host 0.0.0.0 --port 80

# To test the docs part of the parameters
http://127.0.0.1/docs#

# to test the addlist part

http://127.0.0.1/docs#/default/addIntegerlist_addlist_post

With the following parameters

{
  "batchid": "id0101",
  "payload": [
    [
      1,2
    ],[3,4]
  ]
}

# For unit test the functionality
python test_sumelements.py