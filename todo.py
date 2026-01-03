#!/usr/bin/env python3
from todo_service import TodoService

class ToDo:

    def __init__(self):
        todo_service = TodoService()
        pass

    def run_command_parser(self):
        pass

def main():
    compressor = ToDo()
    compressor.run_command_parser()

if __name__ == '__main__':
    main()