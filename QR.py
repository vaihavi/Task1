import qrcode
myqr = qrcode.make("https://youtube.com/shorts/5b_tutKVrM4?si=XVeoY_8NkyYAvhmi")
myqr.save("myqr.png")