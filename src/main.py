from __future__ import annotations

import sys
from typing import Optional


class App:
    """Main application class handling the CLI loop."""

    def __init__(self) -> None:
        self.current_user: Optional[str] = None

    def run(self) -> None:
        """Entry point to start the application."""
        try:
            self._pre_login_loop()
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

    def _pre_login_loop(self) -> None:
        """Display the pre-login menu until the user exits or logs in."""
        while True:
            print("\n=== ToDo CLI ===")
            print("1) Login")
            print("2) Sign Up")
            print("3) Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self._login()
                # placeholder: break if login successful
            elif choice == "2":
                self._sign_up()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

    def _login(self) -> None:
        """Perform a login attempt (stub)."""
        print("Login not implemented yet. Please choose another option.")

    def _sign_up(self) -> None:
        """Perform a sign up attempt (stub)."""
        print("Sign up not implemented yet. Please choose another option.")


def main() -> None:
    app = App()
    app.run()


if __name__ == "__main__":
    main()
