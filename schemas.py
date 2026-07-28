from pydantic import BaseModel
from typing import Optional


# ============================================
# AUTH
# ============================================

class AuthRequest(BaseModel):

    email: str

    password: str


class UserCreate(BaseModel):

    name: str

    email: str

    password: str


# ============================================
# CATEGORY
# ============================================

class Category(BaseModel):

    id: int

    name: str

    class Config:

        from_attributes = True


# ============================================
# PRODUCT
# ============================================

class ProductBase(BaseModel):

    name: str

    description: Optional[str] = None

    price: float

    discount: Optional[float] = 0

    rating: Optional[float] = 0

    image_url: Optional[str] = None

    colors: Optional[str] = None

    sizes: Optional[str] = None

    category_id: Optional[int] = None


class ProductCreate(ProductBase):

    pass


class Product(ProductBase):

    id: int

    class Config:

        from_attributes = True


# ============================================
# CART
# ============================================

class CartItemCreate(BaseModel):

    product_id: int

    quantity: int = 1


class CartItem(BaseModel):

    id: int

    product_id: int

    quantity: int

    user_id: int

    product: Product

    class Config:

        from_attributes = True


# ============================================
# WISHLIST
# ============================================

class WishlistItemCreate(BaseModel):

    product_id: int


class WishlistItem(BaseModel):

    id: int

    user_id: int

    product_id: int

    product: Product

    class Config:

        from_attributes = True