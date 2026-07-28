from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from backend import crud, schemas

from backend.database import get_db


router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


# ============================================
# ADD TO CART
# ============================================

@router.post(
    "/{user_id}",
    response_model=schemas.CartItem
)
def add_product_to_cart(

    user_id: int,

    item: schemas.CartItemCreate,

    db: Session = Depends(get_db)

):

    return crud.add_to_cart(

        db,

        item,

        user_id

    )


# ============================================
# GET CART
# ============================================

@router.get(
    "/{user_id}",
    response_model=list[schemas.CartItem]
)
def get_user_cart(

    user_id: int,

    db: Session = Depends(get_db)

):

    return crud.get_cart(

        db,

        user_id

    )


# ============================================
# REMOVE FROM CART
# ============================================

@router.delete(
    "/{user_id}/{item_id}"
)
def delete_cart_item(

    user_id: int,

    item_id: int,

    db: Session = Depends(get_db)

):

    deleted = crud.remove_from_cart(

        db,

        item_id,

        user_id

    )

    if not deleted:

        raise HTTPException(

            status_code=404,

            detail="Cart item not found"

        )

    return {

        "message": "Item removed from cart"

    }