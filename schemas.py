"""
Database Schemas for NGO site

Each Pydantic model corresponds to a MongoDB collection. The collection name
is the lowercase of the class name.
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

class Galleryitem(BaseModel):
    """
    Gallery items uploaded by admins (images hosted by URL for simplicity)
    Collection name: "galleryitem"
    """
    title: str = Field(..., description="Image title")
    description: Optional[str] = Field(None, description="Short caption or description")
    image_url: HttpUrl = Field(..., description="Publicly accessible image URL")
    tags: Optional[list[str]] = Field(default=None, description="Optional tags")

class News(BaseModel):
    """
    News posts for the NGO
    Collection name: "news"
    """
    title: str = Field(..., description="Headline")
    body: str = Field(..., description="Full article body")
    image_url: Optional[HttpUrl] = Field(None, description="Optional cover image")
    author: Optional[str] = Field(None, description="Author or source")

class Contactmessage(BaseModel):
    """
    Messages sent from the contact form
    Collection name: "contactmessage"
    """
    name: str = Field(..., description="Sender name")
    email: str = Field(..., description="Contact email")
    subject: str = Field(..., description="Message subject")
    message: str = Field(..., description="Message content")
