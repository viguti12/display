makerbit.connect_lcd(39)
makerbit.clear_lcd1602()

def on_forever():
    makerbit.show_string_on_lcd1602("" + str((pins.analog_read_pin(AnalogPin.P3))),
        makerbit.position1602(LcdPosition1602.POS1),
        16)
    makerbit.show_string_on_lcd1602("" + str((pins.analog_read_pin(AnalogPin.P4))),
        makerbit.position1602(LcdPosition1602.POS17),
        16)
basic.forever(on_forever)
