from escpos.printer import Usb

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
p = Usb(0x04b8,0x0e15)
p.text("Hello World\n")
#p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
p.cut()