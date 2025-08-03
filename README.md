# fish-reports

Автоматизация разбора, фильтрации и автозаполнения рыболовных отчетов.  
Проект поддерживает работу через CLI и web-UI (скоро).

## Структура
- `src/` — бизнес-логика
- `fish_reports_ui/` — фронт (Streamlit, FastAPI)
- `data/input/` — входящие файлы
- `data/output/` — результаты
- `data/templates/` — шаблоны

## Запуск

1. Установить зависимости:
    ```bash
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    ```
2. Запустить CLI:
    ```bash
    python src/main.py --help
    ```

3. Запустить UI:
    ```bash
    # Streamlit
    streamlit run fish_reports_ui/app.py

    # FastAPI
    uvicorn fish_reports_ui.app:app --reload
    ```

## Качество кода

- Форматтер: black, ruff
- Тесты: pytest
- Pre-commit хуки настраиваются через pre-commit