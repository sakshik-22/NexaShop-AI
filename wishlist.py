from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from backend import crud

from backend.database import get_db

from backend import schemas


router = APIRouter(

    prefix="/wishlist",

    tags=["Wishlist"]

)


# ============================================
# ADD TO WISHLIST
# ============================================

@router.post(
    "/{user_id}",
    response_model=schemas.WishlistItem
)
def add_to_wishlist(

    user_id: int,

    item: schemas.WishlistItemCreate,

    db: Session = Depends(get_db)

):

    return crud.add_to_wishlist(

        db,

        user_id,

        item.product_id

    )


# ============================================
# GET WISHLIST
# ============================================

@router.get(

    "/{user_id}",

    response_model=list[schemas.WishlistItem]

)
def get_user_wishlist(

    user_id: int,

    db: Session = Depends(get_db)

):

    return crud.get_wishlist(

        db,

        user_id

    )


# ============================================
# REMOVE FROM WISHLIST
# ============================================

@router.delete(

    "/{user_id}/{product_id}"

)
def delete_wishlist_item(

    user_id: int,

    product_id: int,

    db: Session = Depends(get_db)

):

    deleted = crud.remove_from_wishlist(

        db,

        user_id,

        product_id

    )

    if not deleted:

        raise HTTPException(

            status_code=404,

            detail="Wishlist item not found"

        )

    return {

        "message": "Item removed from wishlist"

    }