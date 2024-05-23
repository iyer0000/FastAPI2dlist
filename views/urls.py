from fastapi import status,HTTPException,APIRouter,Request
from utils import get_current_date,validate_output_list,setup_custom_logger
from models.request import RequestModel
from models.response import ResponseModel
from controllers.addlist import execute_process

router = APIRouter()

logger = setup_custom_logger()


@router.post('/addlist',status_code=200,response_model=ResponseModel)
def addIntegerlist(model: RequestModel):
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
        ResponseModel.batchid=batchid
        ResponseModel.response=output
        ResponseModel.status="complete"
        ResponseModel.started_at=start_date
        ResponseModel.completed_at=get_current_date()
        return ResponseModel
            
            