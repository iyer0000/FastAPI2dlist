from fastapi import FastAPI,HTTPException
from db import CreateAdditionModel
from utils import execute_process,get_current_date,validate_output_list,setup_custom_logger

app = FastAPI()

logger = setup_custom_logger('FastAPI_app_for_adding_2dlists')

logger.info('App started')
@app.get('/hello')
def hello():
    logger.info('basic_hello_api')
    return {'message': 'hello'}

@app.post('/addlist',status_code=200)
def addIntegerlist(model: CreateAdditionModel):
    batchid=model.batchid
    input_data=model.payload
    logger.info(f'Rcvd parameters {batchid} and {input_data}')
    start_date=get_current_date()
    output=execute_process(input_data)
    if input_data is None:
        logger.error('Input data is not available')
        raise HTTPException(status_code=409,detail='not found')
    elif validate_output_list(output):
        logger.error('Output data is empty')
        raise HTTPException(status_code=418,detail='Empty output')
    else:
        logger.info(f"Processing is complete with {output}")
        return {
            'batchid':batchid, 
            'response':output,
            "status":"complete",
            "started_at":start_date,
            "completed_at":get_current_date()
            }