from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from backend.database import Base


# ============================================
# CATEGORY
# ============================================

class Category(Base):

    __tablename__ = "categories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    products = relationship(
        "Product",
        back_populates="category"
    )


# ============================================
# PRODUCT
# ============================================

class Product(Base):

    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    price = Column(
        Float,
        nullable=False
    )

    discount = Column(
        Float,
        default=0
    )

    rating = Column(
        Float,
        default=0
    )

    image_url = Column(
        String,
        nullable=True
    )

    colors = Column(
        String,
        nullable=True
    )

    sizes = Column(
        String,
        nullable=True
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id")
    )

    category = relationship(
        "Category",
        back_populates="products"
    )

    cart_items = relationship(
        "CartItem",
        back_populates="product",
        cascade="all, delete-orphan"
    )

    wishlist_items = relationship(
        "WishlistItem",
        back_populates="product",
        cascade="all, delete-orphan"
    )


# ============================================
# USER
# ============================================

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(
        String,
        nullable=False
    )

    cart_items = relationship(
        "CartItem",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    wishlist_items = relationship(
        "WishlistItem",
        back_populates="user",
        cascade="all, delete-orphan"
    )


# ============================================
# CART ITEM
# ============================================

class CartItem(Base):

    __tablename__ = "cart_items"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    quantity = Column(
        Integer,
        default=1
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    user = relationship(
        "User",
        back_populates="cart_items"
    )

    product = relationship(
        "Product",
        back_populates="cart_items"
    )


# ============================================
# WISHLIST ITEM
# ============================================

class WishlistItem(Base):

    __tablename__ = "wishlist_items"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    user = relationship(
        "User",
        back_populates="wishlist_items"
    )

    product = relationship(
        "Product",
        back_populates="wishlist_items"
    )