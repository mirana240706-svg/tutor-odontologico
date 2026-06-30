from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import create_engine, Column, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
import os
from jose import jwt, JWTError

# --- Configuración ---
DATABASE_URL = os.getenv("DATABASE_URL") or os.getenv("POSTGRES_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL o POSTGRES_URL no configurada")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Modelos ---
class UserStateDB(Base):
    __tablename__ = "user_states"
    user_id = Column(String, primary_key=True, index=True)
    state_json = Column(JSON, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# --- App FastAPI ---
app = FastAPI(title="Tutor Odontológico", version="1.0.0")
security = HTTPBearer()
SECRET = os.getenv("NEXTAUTH_SECRET", "fallback_secret_cambiar")
ALGORITHM = "HS256"

async def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security)):
    token = creds.credentials
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Token inválido")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Token expirado o inválido")

@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}

@app.post("/api/start")
async def start_tutorial(profile: dict, user_id: str = Depends(get_current_user)):
    # Simplificado para pruebas
    return {"session_id": user_id, "message": f"Bienvenido {user_id}. Tutor iniciado."}

@app.get("/api/dashboard")
async def get_dashboard(user_id: str = Depends(get_current_user)):
    return {"message": f"Dashboard para {user_id}", "conceptos": ["Crecimiento", "Angle", "Cefalometría"]}