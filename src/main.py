import asyncio

import uvicorn
from fastapi import FastAPI
from reader import preview_excel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Сервис обработки рыболовных отчетов"}


@app.get("/preview/{file_path:path}")
async def preview_file(file_path: str):
    """Предварительный просмотр Excel файла"""
    try:
        df = preview_excel(file_path)
        return {
            "message": "Файл успешно загружен",
            "columns": df.columns.tolist(),
            "rows_count": len(df),
            "preview": df.head().to_dict(orient="records"),
        }
    except Exception as e:
        return {"error": f"Ошибка при чтении файла: {str(e)}"}


async def main():
    # Предварительный просмотр Excel файла при запуске
    # preview_excel("путь_к_вашему_файлу.xlsx")
    preview_excel("/Users/maxviazov/Downloads/משקל .xlsx")

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
