import io
import sys
import time
import random
import traceback

class LoginSystem:
    def __init__(self):
        self.users = {
            "admin": "admin123",
            "guest": "guest"
        }

    def authenticate(self):
        print("=" * 44)
        print("         Welcome to LeOS System         ")
        print("=" * 44)
        attempts = 0
        while attempts < 3:
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            if username in self.users and self.users[username] == password:
                print(f"\n[+] Access Granted. Welcome, {username}!\n")
                time.sleep(0.5)
                return username
            else:
                attempts += 1
                print(f"[-] Invalid credentials. ({3 - attempts} attempts remaining)\n")
        
        print("[-] System Lockout: Too many failed login attempts.")
        return None


class CalculatorApp:
    def run(self):
        print("\n[CALCULATOR]")
        print("Enter standard math expressions (e.g. '12 * (5 + 3)') or type 'back'.\n")
        while True:
            expr = input("calc> ").strip()
            if expr.lower() == 'back':
                break
            try:
                allowed = set("0123456789+-*/(). ")
                if not set(expr).issubset(allowed):
                    print("Error: Only standard math operators and numbers allowed.")
                    continue
                result = eval(expr, {"__builtins__": None}, {})
                print(f"= {result}\n")
            except Exception as e:
                print(f"Error: Invalid expression ({e})\n")


class MessagingApp:
    def __init__(self):
        self.inbox = [
            {"from": "System", "msg": "Welcome to LeOS Messages!"},
            {"from": "Alice", "msg": "Hey! Did you get the LeOS update?"}
        ]

    def run(self, current_user):
        print("\n[MESSAGES]")
        while True:
            print("\n1. View Inbox")
            print("2. Send Message")
            print("3. Back to Main Menu")
            choice = input("Select option (1 - 3): ").strip()

            if choice == "1":
                print("\nINBOX")
                for idx, item in enumerate(self.inbox, 1):
                    print(f"[{idx}] From: {item['from']} | Message: {item['msg']}")
            elif choice == "2":
                recipient = input("To: ").strip()
                text = input("Message: ").strip()
                self.inbox.append({"from": f"Me -> {recipient}", "msg": text})
                print(f"[+] Message sent to {recipient}!")
                
                # Automatic replies
                replies = [
                    "Got your message! Talk soon.",
                    "Sounds awesome!",
                    "I'm in a meeting, will reply later.",
                    "System response received."
                ]
                print(f"[*] {recipient} is typing...")
                time.sleep(1)
                reply = random.choice(replies)
                self.inbox.append({"from": recipient, "msg": reply})
                print(f"[NEW MESSAGE from {recipient}]: {reply}")
            elif choice == "3":
                break


class TicTacToeApp:
    def run(self):
        print("\n[TIC-TAC-TOE]")
        board = [" "] * 9

        def print_board():
            print(f"\n {board[0]} | {board[1]} | {board[2]} ")
            print("---|---|---")
            print(f" {board[3]} | {board[4]} | {board[5]} ")
            print("---|---|---")
            print(f" {board[6]} | {board[7]} | {board[8]} \n")

        def check_win(p):
            wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            return any(board[a] == board[b] == board[c] == p for a,b,c in wins)

        current_player = "X"
        for turn in range(9):
            print_board()
            print(f"Player {current_player}'s turn.")
            while True:
                try:
                    pos = int(input("Enter slot (1 - 9) or 0 to exit: ")) - 1
                    if pos == -1:
                        return
                    if 0 <= pos <= 8 and board[pos] == " ":
                        board[pos] = current_player
                        break
                    else:
                        print("Slot taken or invalid number.")
                except ValueError:
                    print("Please enter a valid slot number (1 - 9).")

            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!\n")
                return

            current_player = "O" if current_player == "X" else "X"

        print_board()
        print("It's a draw!\n")


class SystemInfoApp:
    def run(self, user):
        print("\n[SYSTEM MONITOR]")
        print(f"Logged-in User : {user}")
        print(f"OS Version     : LeOS 1.0 (Numeric Shell)")
        print(f"CPU Load       : {random.randint(10, 48)}%")
        print(f"RAM Usage      : {random.randint(210, 480)} MB / 1024 MB")
        print(f"System Uptime  : {random.randint(1, 99)} minutes")
        input("\nPress 'ENTER' to return to desktop...")
      				
class CodeEditor:
    def __init__(self):
        self.files = {
            "hello.py": 'print("Hello from LeOS Desktop!")\nfor i in range(3):\n    print(f"Step {i+1}")',
            "math_demo.py": 'def factorial(n):\n    return 1 if n <= 1 else n * factorial(n - 1)\n\nprint("Factorial of 5:", factorial(5))'
        }

    def run(self):
        print("\nLeOS Code Editor & Runtime Environment")
        while True:
            print("\n[LeOS Code Editor Menu]")
            print("1. List & Run Saved Scripts")
            print("2. Create / Edit Script")
            print("3. View Script Source Code")
            print("4. Quick REPL Environment")
            print("5. Delete Script")
            print("6. Return to Desktop")

            choice = input("Select option (1 - 6): ").strip()

            if choice == "1":
                self._list_and_run()
            elif choice == "2":
                self._create_or_edit()
            elif choice == "3":
                self._view_script()
            elif choice == "4":
                self._repl()
            elif choice == "5":
                self._delete_script()
            elif choice == "6":
                print("Returning to Desktop...")
                break
            else:
                print("[-] Invalid choice. Please select a number from 1 to 6.")

    def _list_and_run(self):
        if not self.files:
            print("[-] No scripts available.")
            return

        print("\nAvailable Scripts")
        file_list = list(self.files.keys())
        for idx, name in enumerate(file_list, 1):
            print(f"  {idx}. {name}")

        try:
            sel = int(input("\nSelect script to execute (0 to cancel): ")) - 1
            if sel == -1:
                return
            if 0 <= sel < len(file_list):
                filename = file_list[sel]
                self._execute(filename, self.files[filename])
            else:
                print("[-] Invalid selection.")
        except ValueError:
            print("[-] Please enter a valid number.")

    def _create_or_edit(self):
        filename = input("\nEnter script filename (e.g. script.py): ").strip()
        if not filename:
            return
        if not filename.endswith(".py"):
            filename += ".py"

        existing_code = self.files.get(filename, "")
        lines = existing_code.split("\n") if existing_code else []

        print(f"\nEditing '{filename}'")
        print("Commands: ':save' (Save & Exit), ':cancel' (Discard), ':list' (Show Lines)")
        print("Edit line: ':line <num> <content>'")
        print("Enter code lines below:\n")

        if lines:
            self._print_lines(lines)

        line_num = len(lines) + 1
        while True:
            entry = input(f"{line_num:02d} | ")
            stripped = entry.strip()

            if stripped == ":save":
                self.files[filename] = "\n".join(lines)
                print(f"\n[+] Saved '{filename}' ({len(lines)} lines).")
                if input("Run script now? (Y/N): ").strip().upper() == 'Y':
                    self._execute(filename, self.files[filename])
                break
            elif stripped == ":cancel":
                print("\n[-] Discarded changes.")
                break
            elif stripped == ":list":
                self._print_lines(lines)
                continue
            elif stripped.startswith(":line "):
                parts = stripped.split(" ", 2)
                try:
                    target_idx = int(parts[1]) - 1
                    new_val = parts[2] if len(parts) > 2 else ""
                    if 0 <= target_idx < len(lines):
                        lines[target_idx] = new_val
                        print(f"[+] Updated line {target_idx + 1}.")
                    else:
                        print("[-] Line number out of range.")
                except (ValueError, IndexError):
                    print("[-] Usage: :line <line_number> <content>")
                continue
            
            lines.append(entry)
            line_num += 1

    def _view_script(self):
        if not self.files:
            print("[-] No scripts available.")
            return

        file_list = list(self.files.keys())
        for idx, name in enumerate(file_list, 1):
            print(f"  {idx}. {name}")

        try:
            sel = int(input("\nSelect script to view (0 to cancel): ")) - 1
            if sel == -1:
                return
            if 0 <= sel < len(file_list):
                filename = file_list[sel]
                print(f"\nSource Code: {filename}")
                lines = self.files[filename].split("\n")
                self._print_lines(lines)
        except ValueError:
            print("[-] Invalid input.")

    def _delete_script(self):
        if not self.files:
            print("[-] No scripts available.")
            return

        file_list = list(self.files.keys())
        for idx, name in enumerate(file_list, 1):
            print(f"  {idx}. {name}")

        try:
            sel = int(input("\nSelect script to delete (0 to cancel): ")) - 1
            if sel == -1:
                return
            if 0 <= sel < len(file_list):
                removed = file_list[sel]
                del self.files[removed]
                print(f"[+] Deleted '{removed}'.")
        except ValueError:
            print("[-] Invalid input.")

    def _repl(self):
        print("\nPython Quick REPL")
        print("Type single-line Python statements/expressions. Type 'exit' to quit.\n")
        env = {"__name__": "__main__"}
        while True:
            code = input(">>> ").strip()
            if code == "exit":
                break
            if not code:
                continue
            try:
                result = eval(code, env)
                if result is not None:
                    print(result)
            except SyntaxError:
                try:
                    exec(code, env)
                except Exception as e:
                    print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")

    def _execute(self, filename, code_str):
        print(f"\n[RUNNING: {filename}]")
        buffer = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = buffer

        exec_scope = {"__name__": "__main__"}
        error_msg = None

        try:
            exec(code_str, exec_scope)
        except Exception:
            error_msg = traceback.format_exc()
        finally:
            sys.stdout = old_stdout

        output = buffer.getvalue()
        if output:
            print("Output")
            print(output.rstrip())
        if error_msg:
            print("Execution Error")
            print(error_msg.rstrip())
        print("[FINISHED]\n")

    def _print_lines(self, lines):
        for idx, line in enumerate(lines, 1):
            print(f"  {idx:02d} | {line}")

class LeOS:
    def __init__(self):
        self.auth = LoginSystem()
        self.calc = CalculatorApp()
        self.messenger = MessagingApp()
        self.tictactoe = TicTacToeApp()
        self.sys_info = SystemInfoApp()
        self.code_editor = CodeEditor()

    def boot(self):
        user = self.auth.authenticate()
        if not user:
            return

        while True:
            print("\n==========================================")
            print(f"    LeOS Desktop  |  User: {user}")
            print("==========================================")
            print(" 1. Calculator")
            print(" 2. Messages")
            print(" 3. Tic-Tac-Toe")
            print(" 4. System Monitor")
            print(" 5. Code Editor")
            print(" 6. Switch User / Log Out")
            print(" 7. Shutdown System")
            print("==========================================")
            
            choice = input("Select an app (1 - 7): ").strip()

            if choice == "1":
                self.calc.run()
            elif choice == "2":
                self.messenger.run(user)
            elif choice == "3":
                self.tictactoe.run()
            elif choice == "4":
                self.sys_info.run(user)
            elif choice == "5":
                self.code_editor.run()
            elif choice == "6":
                print("Logging out...")
                time.sleep(0.5)
                self.boot()
                break
            elif choice == "7":
                print("\nShutting down LeOS...")
                time.sleep(1)
                break
            else:
                print("[-] Invalid input. Please select a number from 1 to 7.")


if __name__ == "__main__":
    LeOS().boot()
    