from fastapi import (
    FastAPI,
    Depends,
    HTTPException
)

from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session


from backend import models

from backend import crud

from backend import schemas


from backend.database import (
    engine,
    get_db
)


from backend.routers import (
    products,
    cart,
    wishlist
)

# ============================================
# DATABASE TABLES
# ============================================

models.Base.metadata.create_all(
    bind=engine
)


# ============================================
# FASTAPI APP
# ============================================

app = FastAPI(

    title="AI E-commerce Recommendation API",

    version="1.0.0"

)


# ============================================
# CORS
# ============================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


# ============================================
# ROUTERS
# ============================================

app.include_router(

    products.router

)

app.include_router(

    cart.router

)

app.include_router(

    wishlist.router

)

# ============================================
# STARTUP
# ============================================

@app.on_event("startup")
def startup():

    db = next(get_db())

    try:

        crud.init_mock_data(db)

    finally:

        db.close()


# ============================================
# HEALTH
# ============================================

@app.get("/health")
def health_check():

    return {

        "status": "healthy",

        "message": "API is running"

    }


# ============================================
# LOGIN
# ============================================

@app.post("/login")
def login(

    req: schemas.AuthRequest,

    db: Session = Depends(get_db)

):

    user = crud.get_user_by_email(

        db,

        req.email

    )

    if not user:

        raise HTTPException(

            status_code=400,

            detail="Email not found"

        )

    if user.hashed_password != req.password:

        raise HTTPException(

            status_code=400,

            detail="Incorrect password"

        )

    return {

        "token": "fake-jwt-token",

        "user": {

            "id": user.id,

            "name": user.name

        }

    }


# ============================================
# REGISTER
# ============================================

@app.post("/register")
def register(

    req: schemas.UserCreate,

    db: Session = Depends(get_db)

):

    existing_user = crud.get_user_by_email(

        db,

        req.email

    )

    if existing_user:

        raise HTTPException(

            status_code=400,

            detail="Email already registered"

        )

    user = crud.create_user(

        db,

        req

    )

    return {

        "token": "fake-jwt-token",

        "user": {

            "id": user.id,

            "name": user.name

        }

    }


# ============================================
# CATEGORIES
# ============================================

@app.get(

    "/categories",

    response_model=list[schemas.Category]

)
def get_categories(

    db: Session = Depends(get_db)

):

    return crud.get_categories(db)