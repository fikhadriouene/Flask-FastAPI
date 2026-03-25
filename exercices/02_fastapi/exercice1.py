# ## Exercice 1: Modèle Utilisateur Basique

# **Énoncé**:
# Créez un modèle Pydantic `User` avec:
# - `id`: entier (non modifiable)
# - `username`: chaîne (2-50 caractères)
# - `email`: email valide
# - `age`: entier optionnel (0-150 si fourni)
# - `is_active`: booléen (par défaut True)

# Testez avec une route POST `/users` qui accepte le modèle.

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

app = FastAPI()

next_user_id = 2

users_db = {
    1: {
        "id": 1,
        "username": "Alice Johnson",
        "email": "alice@example.com",
        "age": 28,
        "is_active": True,
        "created_at": "2024-01-15T10:30:00Z"
    }
}

class User(BaseModel):
    """User model with validation"""
    id: int = Field(..., frozen=True)
    username: str = Field(..., min_length=2, max_length=50, description="Username")
    email: EmailStr = Field(..., description="User's email address")
    age: Optional[int] = Field(None, ge=0, le=150, description="User's age (0-150)")
    is_active: bool = Field(default=True, description="Is user active?")

class UserResponse(BaseModel):
    """Response model for user"""
    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: str

@app.post("/users", response_model=UserResponse, status_code=201, tags=["Users"])
def create_user(user: User):
    global next_user_id

    new_user = {
        "id": next_user_id,
        "username": user.username,
        "email": user.email,
        "age": user.age,
        "is_active": user.is_active,
        "created_at": datetime.utcnow().isoformat() + "Z"
    }
    users_db[next_user_id] = new_user
    next_user_id += 1

    return new_user

@app.get("/users")
def get_users():
    return list(users_db.values())





