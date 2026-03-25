# ## Exercice 2: Validateurs Personnalisés

# **Énoncé**:
# Créez un modèle `Password` avec validation:
# - `password`: au moins 8 caractères, doit contenir minuscule, majuscule, chiffre, symbole
# - `confirm_password`: doit égaler `password`

# Retournez des erreurs détaillées si la validation échoue.

# Exemple:
# ```bash
# # Valide
# {"password": "SecurePass123!", "confirm_password": "SecurePass123!"}

# # Invalide
# {"password": "weak", "confirm_password": "weak"}
# # Erreur: "password too short"
# ```

from fastapi import FastAPI
from pydantic import BaseModel, field_validator, model_validator
import re
import uvicorn

app = FastAPI()

class Password(BaseModel):
    password: str
    confirm_password: str

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("password too short")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError("Password must contain at least one special character")
        return v

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("confirm_password must match password")
        return self

@app.post("/password")
def validate_password(data: Password):
    return {"message": "Password is valid"}

if __name__ == "__main__":
    uvicorn.run("exercice2:app", host="127.0.0.1", port=8000, reload=True)