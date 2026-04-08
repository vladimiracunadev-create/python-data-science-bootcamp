from app.execution_engine import execute_code, reset_session


def test_execute_code_keeps_state_between_cells():
    reset_session("demo")
    execute_code("demo", "x = 10")
    result = execute_code("demo", "x + 5")
    assert result["result"] == "15"


def test_execute_code_captures_stdout():
    reset_session("stdout")
    result = execute_code("stdout", 'print("hola")')
    assert "hola" in result["stdout"]
