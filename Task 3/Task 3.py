c = 0 # глобальная переменная

def add():
    global c
    c = c + 2 # прибавляем 2 к c
    print("Внутри функции add():", c)

add()
print("В глобальной области видимости:", c)