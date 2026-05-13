from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task

hub = PrimeHub()
left_drive = Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.A)
robot = DriveBase(
    left_drive,
    right_drive,
    wheel_diameter=56,
    axle_track=128
)

hub.system.set_stop_button(Button.BLUETOOTH)


async def my_run():
    robot.straight(1000)
    await wait(5000)  # simulates a long run

async def cancel_watcher():
    while True:
        if Button.CENTER in hub.buttons.pressed():
            return  # returning cancels sibling tasks
        await wait(50)

async def main():
    pressed = []
    while True:
        was_pressed = pressed
        pressed = hub.buttons.pressed()

        if Button.CENTER in pressed and Button.CENTER not in was_pressed:
            await multitask(my_run(), cancel_watcher(), race=True)

        await wait(50)

run_task(main())
