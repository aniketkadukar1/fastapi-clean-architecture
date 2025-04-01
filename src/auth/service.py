from datetime import datetime, timedelta, timezone
from typing import Annotated
from uuid import UUID, uuid4
from fastapi import Depends
from passlib.context import CryptContext
import jwt
from jwt import PyJWTError
from sqlalchemy.orm import Session
from src.entities.user import User
from . import model
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..exceptions import AuthenticationError




