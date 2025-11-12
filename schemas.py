"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Clinic-specific schemas

class Inquiry(BaseModel):
    """
    Inquiries from website contact/booking form
    Collection name: "inquiry"
    """
    name: str = Field(..., min_length=2, description="Full name of the person")
    email: EmailStr = Field(..., description="Email address for follow-up")
    phone: Optional[str] = Field(None, description="Contact phone number")
    service_type: Optional[str] = Field(None, description="Service interested in (e.g., Hearing Assessment, Speech Therapy)")
    subject: Optional[str] = Field(None, description="Short subject or reason")
    message: str = Field(..., min_length=5, max_length=2000, description="Message or additional details")
    preferred_date: Optional[str] = Field(None, description="Preferred appointment date as string (YYYY-MM-DD)")
