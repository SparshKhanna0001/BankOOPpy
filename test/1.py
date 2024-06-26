"""
    The porgram tests a class when self isn't passed as an argument.
"""

class Test:

    @staticmethod
    def test(x)-> None:
        print(x)
    
i, k = Test(), Test()
i.test(5)
# k.test()

print("when a method of a class is called,what it does it passes two parameters, the obj itself and the another parameter passed as in the above case therefore it results into an error that two positional args passed but one is expected. but when static method constructor isnused it is resolved.")
"""
def h(l):
    print(l)

h()

"""

