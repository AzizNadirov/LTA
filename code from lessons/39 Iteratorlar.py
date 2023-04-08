# Iteratorlar


# iterasiya oluna bilən obyektlərin `__iter__` metodu var.
# hansı ki geriyə həmin obyektin `iteratorunu` qaytarır.
# `next(iterator)` ilə `iterator` obyektinin növbəti elementini ala bilirik.
# iterator hə müraciətdə qaytarılacaq elementi yadda saxlayır və hər next() müraciətində
# növbəti elementi qaytarır. Əgər bütün elementlər artıq qaytarılıbsa - `StopIteartion` xətası baş verir.




l = [1,2,3]
l_iter = iter(l)        # l_iter = l_iter.__iter__()

print(next(l_iter)) # 1
print(next(l_iter)) # 2
print(next(l_iter)) # 3
print(next(l_iter)) # StopIteartion


# iterasiya oluna bilən obyektlərin `__iter__` metodu var.
# hansı ki geriyə həmin obyektin `iteratorunu` qaytarır.
# `next(iterator)` ilə `iterator` obyektinin növbəti elementini ala bilirik.
# iterator hə müraciətdə qaytarılacaq elementi yadda saxlayır və hər next() müraciətində
# növbəti elementi qaytarır. Əgər bütün elementlər artıq qaytarılıbsa - `StopIteartion` xətası baş verir.




