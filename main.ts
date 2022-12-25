input.onButtonPressed(Button.A, function () {
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 100)
    basic.pause(2000)
    Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.Left, 50)
    basic.pause(1000)
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 75)
    basic.pause(2000)
    Kitronik_Move_Motor.stop()
})
input.onButtonPressed(Button.B, function () {
    Kitronik_Move_Motor.stop()
})
Kitronik_Move_Motor.beepHorn()
Kitronik_Move_Motor.beepHorn()
basic.forever(function () {
	
})
