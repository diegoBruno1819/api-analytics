from fastapi import APIRouter
from app.schemas.sale import Sale

router = APIRouter(prefix="/sales", tags=["sales"])

@router.post("/", response_model=Sale, status_code=201)
def create_sale(sale: Sale):
    return sale
