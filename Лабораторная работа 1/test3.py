# TODO Найдите количество книг, которое можно разместить на дискете
start_value = 1.44
page =  100
line = 50
chars = 25
charWeight = 4
lineByte = charWeight * chars  # в 1 строке 100 байт

pageByte = lineByte * line  # в 1 странице 50 00 байт

bookbyte = pageByte * page # в 1 книге 500 000 байт

answer = (start_value * 1024 * 1024) // bookbyte

print("Количество книг, помещающихся на дискету:", int(answer))


# 3 книги