import builtins
from io import StringIO

from src.main import App
# from main import App



def run_menu_with_inputs(inputs):
    """Helper to simulate user inputs for the pre-login menu."""
    app = App()
    input_iter = iter(inputs)
    captured = StringIO()

    def fake_input(prompt=""):
        try:
            value = next(input_iter)
        except StopIteration:
            raise EOFError
        # echo the prompt and value so tests can inspect them if needed
        print(prompt + value, file=captured)
        return value

    old_input = builtins.input
    try:
        builtins.input = fake_input
        # capture stdout from the loop as well
        from contextlib import redirect_stdout

        with redirect_stdout(captured):
            app._pre_login_loop()
    finally:
        builtins.input = old_input

    return captured.getvalue()


def test_exit_option_terminates_loop():
    output = run_menu_with_inputs(["3"])
    assert "Goodbye!" in output


def test_invalid_choice_shows_message():
    output = run_menu_with_inputs(["x", "3"])
    assert "Invalid choice" in output


def test_login_and_signup_stubs():
    output = run_menu_with_inputs(["1", "2", "3"])
    assert "Login not implemented" in output
    assert "Sign up not implemented" in output


def test_app_initialization():
    app = App()
    assert app.current_user is None
