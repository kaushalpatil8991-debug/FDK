"""Standalone entry point: the fdk detector on its own FastAPI app (port 8080 in Docker).

Inside the Candor backend the same two calls (fdk_lifespan, fdk_mount) are made from the
backend's main.py; here they are the whole app. Set FDK_ENABLED=true and the other FDK_*
variables (see fdk_env.example) in the container's environment.

Routes: GET /fdk/health, POST /fdk/webhook/telegram, /fdk/mcp (see fdk_main.py).
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from fdk_main import fdk_lifespan, fdk_mount


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with fdk_lifespan():
        yield


app = FastAPI(title="fdk — Shoonya volume-spike detector", lifespan=lifespan)


@app.get("/")
async def root():
    return {"service": "fdk", "health": "/fdk/health"}


fdk_mount(app)
