makerbit.connectLcd(39)
makerbit.clearLcd1602()
basic.forever(function () {
    makerbit.showStringOnLcd1602("Hola mama, feliz", makerbit.position1602(LcdPosition1602.Pos1), 16)
    makerbit.showStringOnLcd1602("dia. Te queremos", makerbit.position1602(LcdPosition1602.Pos17), 16)
})
