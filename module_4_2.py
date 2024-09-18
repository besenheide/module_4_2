def test_function():
    def inner_function():
        print('Я в области видимости test_function')

    inner_function()


test_function()

try:
    inner_function()
except:
    print('Здесь нельзя вызвать inner_function')
