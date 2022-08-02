origial = "tizas"
nueva = "yesos"

nombreF = "fichero.txt"

f = open(nombreF, "r")

texto_original = f.read()
f.close()

texto_sutituido = texto_original.replace(origial, nueva)

f = open(nombreF, "w")
f.write(texto_sutituido)
f.close()