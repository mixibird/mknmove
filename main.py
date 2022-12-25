def on_button_pressed_a():
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 100)
    basic.pause(2000)
    Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.LEFT, 50)
    basic.pause(1000)
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 75)
    basic.pause(2000)
    Kitronik_Move_Motor.stop()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Kitronik_Move_Motor.stop()
input.on_button_pressed(Button.B, on_button_pressed_b)

Kitronik_Move_Motor.beep_horn()
Kitronik_Move_Motor.beep_horn()

def on_forever():
    pass
basic.forever(on_forever)
