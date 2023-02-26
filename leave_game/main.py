import keyboard


def stop():
    keyboard.unhook_all()
    print("Script stopped.")
    quit()


def leave_script():
    from leave_script import leave_game
    leave_game(0.10)


if __name__ == '__main__':
    keyboard.add_hotkey('F5', leave_script)
    keyboard.add_hotkey('F6', stop)
    keyboard.wait()
