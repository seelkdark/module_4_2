def test_function():
    # Внутренняя функция, которая печатает сообщение
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов внутренней функции внутри test_function
    inner_function()

# Вызов тестовой функции, чтобы увидеть результат
test_function()