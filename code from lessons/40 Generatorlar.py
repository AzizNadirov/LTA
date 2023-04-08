# Generatorlar



# million_list = list(range(10**6))


# million_rg = range(10**6)       # generator


# def sqr_range(start, stop):
#     for i in range(start, stop):
#         yield i ** 2
    

# sqr_generator = sqr_range(0, 10**3)


# for i in sqr_range(0, 10**3):
#     print(i)
#     if i == 100:
#         break


# print((i ** 2 for i in range(10)))




def f():
    while True:
        print('before')
        yield 0
        print('after')



it = iter(f())
for i in range(3):
    next(it)
    print('---------')



