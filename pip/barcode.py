import barcode

hr = barcode.get_barcode_class('EAN13')
Hr = hr('1234567891012')
qr = Hr.save('123')