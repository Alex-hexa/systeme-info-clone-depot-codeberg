def function_1(num):

    def function_2(num2):
        return num + num2

    return function_2

ref = function_1(10)
print(ref)
print(ref(12))