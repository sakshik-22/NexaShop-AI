from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from backend import crud, schemas

from backend.database import get_db

from backend.recommendation import get_similar_products


router = APIRouter(

    prefix="/products",

    tags=["Products"]

)


# ============================================
# GET ALL PRODUCTS
# ============================================

@router.get(

    "/",

    response_model=list[schemas.Product]

)
def get_all_products(

    skip: int = 0,

    limit: int = 200,

    db: Session = Depends(get_db)

):

    return crud.get_products(

        db,

        skip=skip,

        limit=limit

    )


# ============================================
# GET PRODUCTS BY CATEGORY
# ============================================

@router.get(

    "/category/{category_id}",

    response_model=list[schemas.Product]

)
def get_products_by_category(

    category_id: int,

    db: Session = Depends(get_db)

):

    return crud.get_products_by_category(

        db,

        category_id

    )


# ============================================
# GET SIMILAR PRODUCTS
# ============================================

@router.get(

    "/{product_id}/similar",

    response_model=list[schemas.Product]

)
def get_similar_product_list(

    product_id: int,

    limit: int = 6,

    db: Session = Depends(get_db)

):

    product = crud.get_product(

        db,

        product_id

    )

    if not product:

        raise HTTPException(

            status_code=404,

            detail="Product not found"

        )


    return get_similar_products(

        db,

        product_id,

        limit

    )


# ============================================
# GET SINGLE PRODUCT
# ============================================

@router.get(

    "/{product_id}",

    response_model=schemas.Product

)
def get_single_product(

    product_id: int,

    db: Session = Depends(get_db)

):

    product = crud.get_product(

        db,

        product_id

    )

    if not product:

        raise HTTPException(

            status_code=404,

            detail="Product not found"

        )

    return product


# ============================================
# CREATE PRODUCT
# ============================================

@router.post(

    "/",

    response_model=schemas.Product

)
def create_product(

    product: schemas.ProductCreate,

    db: Session = Depends(get_db)

):

    return crud.create_product(

        db,

        product

    )