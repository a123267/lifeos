from sqlalchemy import inspect, text

from backend.app.database import engine
import backend.app.models


def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT DATABASE()")
        ).scalar()

    assert result == "lifeos"


def test_required_tables_exist():
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    expected_tables = {
        "tasks",
        "habits",
        "habit_logs",
        "weekly_goals",
        "activity_events",
        "pipeline_runs"
    }

    assert expected_tables.issubset(set(existing_tables))
