#!/usr/bin/env python3
import sys

from todo_service import TodoService

class Todo:

    def __init__(self):
        self.todo_service = TodoService()
        self.commands = {
            'quit': self._quit,
            'add': self.todo_service.add,
            'remove': self.todo_service.remove,
            'list': self.todo_service.list,
            'cd': self.todo_service.cd,
        }

    def _quit(self, args=''):
        sys.exit(0)

    def run_command_parser(self):
        while True:
            try:
                print(f'{self.todo_service.get_path()}> ', end='', flush=True)
                line = input().strip()

                if not line:
                    continue

                parts = line.split(' ', maxsplit=1)
                command = parts[0]
                args = parts[1] if len(parts) > 1 else ''

                if command in self.commands:
                    self.commands[command](args)
                else:
                    print(f"Unknown command: {command}")

            except (KeyboardInterrupt, EOFError):
                break
            except Exception as e:
                print(f"Error: {e}")


def main():
    todo = Todo()
    todo.run_command_parser()


if __name__ == '__main__':
    main()