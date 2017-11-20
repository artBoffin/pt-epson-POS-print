#!/usr/bin/python
# -*- coding: UTF8 -*-
from escpos.printer import Usb

p = Usb(0x04b8,0x0e15)
p.set(font='a', height=1, align='center')
p.text("Font a\n")
p.set(font='b', height=1, align='center')
p.text("Font b\n")
p.set(font='a', height=1, align='center')
p.text("--------------------------------\n")
p.set(font='a', height=2, align='center')
p.text("Font a height 2\n")
p.set(font='b', height=2, align='center')
p.text("Font b height 2\n")
p.qr("This QR code is readable by phone")
p.cut()