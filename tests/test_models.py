from datetime import datetime

from src.models import TodoItem, Priority, Status
# from models import TodoItem, Priority, Status


def test_todoitem_defaults_and_types():
    item = TodoItem(title="Test")

    assert item.id is not None and isinstance(item.id, str)
    assert item.title == "Test"
    assert item.details == ""
    assert item.priority == Priority.MID
    assert item.status == Status.PENDING
    assert item.owner == ""

    # created_at and updated_at are ISO-8601 strings
    datetime.fromisoformat(item.created_at)
    datetime.fromisoformat(item.updated_at)


def test_priority_enum_str_conversion():
    item = TodoItem(title="Foo", priority="HIGH")
    assert item.priority == Priority.HIGH


def test_status_enum_str_conversion():
    item = TodoItem(title="Foo", status="COMPLETED")
    assert item.status == Status.COMPLETED


def test_enum_instances_are_preserved():
    # passing enum members directly should work without conversion
    item = TodoItem(title="Bar", priority=Priority.HIGH, status=Status.COMPLETED)
    assert item.priority is Priority.HIGH
    assert item.status is Status.COMPLETED


def test_ids_are_unique_across_items():
    ids = {TodoItem(title=f"i{i}").id for i in range(10)}
    assert len(ids) == 10  # no collisions


def test_timestamp_ordering_and_format():
    item = TodoItem(title="Time")
    created = datetime.fromisoformat(item.created_at)
    updated = datetime.fromisoformat(item.updated_at)
    # by default they should be very close; created <= updated
    assert created <= updated


def test_invalid_priority_str_raises_value_error():
    try:
        TodoItem(title="Test", priority="INVALID")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_invalid_status_str_raises_value_error():
    try:
        TodoItem(title="Test", status="INVALID")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
