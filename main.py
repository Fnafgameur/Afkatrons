import os
import time
import yaml
import pyautogui

from pynput.mouse import Button, Controller

config_file = "config"
kb = pyautogui
mouse = Controller()


def main():
    check_file()
    config = get_config()

    time.sleep(config.get_time_script_start())

    while True:

        # Forward
        kb.keyDown(config.get_forward())
        time.sleep(config.get_time_to_hold_key())
        kb.keyUp(config.get_forward())

        time.sleep(config.get_time_between_inputs())

        # Right
        kb.keyDown(config.get_right())
        time.sleep(config.get_time_to_hold_key())
        kb.keyUp(config.get_right())

        time.sleep(config.get_time_between_inputs())

        # Backward
        kb.keyDown(config.get_backward())
        time.sleep(config.get_time_to_hold_key())
        kb.keyUp(config.get_backward())

        time.sleep(config.get_time_between_inputs())

        # Left
        kb.keyDown(config.get_left())
        time.sleep(config.get_time_to_hold_key())
        kb.keyUp(config.get_left())

        time.sleep(config.get_time_between_inputs())

        # Jump
        kb.keyDown(config.get_jump())
        time.sleep(config.get_time_to_hold_key())
        kb.keyUp(config.get_jump())

        time.sleep(config.get_time_between_inputs())

        # Left click
        if config.get_do_left_click():
            mouse.click(Button.left, 1)
            time.sleep(config.get_time_between_inputs())


def check_file():
    if os.path.exists("config.yml"):
        return

    with open("config.yml", "w") as f:

        f.write("# Movement keys\n")
        f.write("forward: z\n")
        f.write("left: q\n")
        f.write("backward: s\n")
        f.write("right: d\n")
        f.write("jump: space\n")

        f.write("\n# Times (in sec (e.g : 0.5, 1, 1.78)\n")
        f.write("time-script-start: 3\n")
        f.write("time-between-inputs: 1\n")
        f.write("time-to-hold-key: 1\n")

        f.write("\n# Mouse control\n")
        f.write("do-left-click: true\n")


def get_config():
    with (open("config.yml", "r") as f):
        data = yaml.load(f, Loader=yaml.FullLoader)

        return Inputs(data["forward"],
                      data["left"],
                      data["backward"],
                      data["right"],
                      data["jump"],
                      float(data["time-between-inputs"]),
                      float(data["time-to-hold-key"]),
                      float(data["time-script-start"]),
                      bool(data["do-left-click"]))


class Inputs:

    def __init__(self, forward, left, backward, right, jump, time_between_inputs, time_to_hold_key, time_script_start, do_left_click):
        self.forward = forward
        self.left = left
        self.backward = backward
        self.right = right
        self.jump = jump
        self.time_between_inputs = time_between_inputs
        self.time_to_hold_key = time_to_hold_key
        self.time_script_start = time_script_start
        self.do_left_click = do_left_click

    def get_forward(self):
        return self.forward

    def get_left(self):
        return self.left

    def get_backward(self):
        return self.backward

    def get_right(self):
        return self.right

    def get_jump(self):
        return self.jump

    def get_time_between_inputs(self):
        return self.time_between_inputs

    def get_time_to_hold_key(self):
        return self.time_to_hold_key

    def get_do_left_click(self):
        return self.do_left_click

    def get_time_script_start(self):
        return self.time_script_start


if __name__ == '__main__':
    main()
