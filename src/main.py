import asyncio

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Сервис обработки рыболовных отчетов"}


async def main():
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
    server = uvicorn.Server(config)
    try:
        await server.serve()
    except Exception as e:
        print(f"Ошибка при запуске сервера: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
