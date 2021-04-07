from typing import Optional, List, Union

from uuid import UUID
from datetime import datetime, time, timedelta

from enum import Enum

from fastapi import FastAPI, Query, Body, Path, Depends, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

from .gettingStarted import app

client = TestClient(app)

def test_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "Hello": "World"}