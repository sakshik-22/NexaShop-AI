from sqlalchemy.orm import Session

from backend import models, schemas


# ============================================
# USERS
# ============================================

def get_user_by_email(
    db: Session,
    email: str
):

    return (
        db.query(models.User)
        .filter(
            models.User.email == email
        )
        .first()
    )


def create_user(
    db: Session,
    user: schemas.UserCreate
):

    db_user = models.User(

        name=user.name,

        email=user.email,

        hashed_password=user.password

    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


# ============================================
# PRODUCTS
# ============================================

def get_product(
    db: Session,
    product_id: int
):

    return (
        db.query(models.Product)
        .filter(
            models.Product.id == product_id
        )
        .first()
    )


def get_products(
    db: Session,
    skip: int = 0,
    limit: int = 200
):

    return (
        db.query(models.Product)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_product(
    db: Session,
    product: schemas.ProductCreate
):

    db_product = models.Product(
        **product.model_dump()
    )

    db.add(db_product)

    db.commit()

    db.refresh(db_product)

    return db_product


def get_products_by_category(
    db: Session,
    category_id: int
):

    return (
        db.query(models.Product)
        .filter(
            models.Product.category_id == category_id
        )
        .all()
    )


# ============================================
# CATEGORIES
# ============================================

def get_categories(
    db: Session
):

    return (
        db.query(models.Category)
        .all()
    )


# ============================================
# CART
# ============================================

def add_to_cart(
    db: Session,
    item: schemas.CartItemCreate,
    user_id: int
):

    db_item = (
        db.query(models.CartItem)
        .filter(
            models.CartItem.user_id == user_id,
            models.CartItem.product_id == item.product_id
        )
        .first()
    )

    if db_item:

        db_item.quantity += item.quantity

    else:

        db_item = models.CartItem(

            product_id=item.product_id,

            quantity=item.quantity,

            user_id=user_id

        )

        db.add(db_item)

    db.commit()

    db.refresh(db_item)

    return db_item


def get_cart(
    db: Session,
    user_id: int
):

    return (
        db.query(models.CartItem)
        .filter(
            models.CartItem.user_id == user_id
        )
        .all()
    )


def remove_from_cart(
    db: Session,
    item_id: int,
    user_id: int
):

    db_item = (
        db.query(models.CartItem)
        .filter(
            models.CartItem.id == item_id,
            models.CartItem.user_id == user_id
        )
        .first()
    )

    if not db_item:

        return False

    db.delete(db_item)

    db.commit()

    return True


# ============================================
# STARTUP
# ============================================

def init_mock_data(
    db: Session
):

    return


# ============================================
# WISHLIST
# ============================================

def add_to_wishlist(
    db: Session,
    user_id: int,
    product_id: int
):

    existing_item = (
        db.query(
            models.WishlistItem
        )
        .filter(
            models.WishlistItem.user_id == user_id,
            models.WishlistItem.product_id == product_id
        )
        .first()
    )

    if existing_item:

        return existing_item

    wishlist_item = models.WishlistItem(

        user_id=user_id,

        product_id=product_id

    )

    db.add(wishlist_item)

    db.commit()

    db.refresh(wishlist_item)

    return wishlist_item


def get_wishlist(
    db: Session,
    user_id: int
):

    return (
        db.query(
            models.WishlistItem
        )
        .filter(
            models.WishlistItem.user_id == user_id
        )
        .all()
    )


def remove_from_wishlist(
    db: Session,
    user_id: int,
    product_id: int
):

    item = (
        db.query(
            models.WishlistItem
        )
        .filter(
            models.WishlistItem.user_id == user_id,
            models.WishlistItem.product_id == product_id
        )
        .first()
    )

    if not item:

        return False

    db.delete(item)

    db.commit()

    return True