# Xətaların idarə edilməsi - try-except-else-finally; raise; assert

# try:
#     file_stream = open('somefile.txt')      # FileNotFoundError
#     print(file_stream.read())

# except ZeroDivisionError:
#     pass

# except FileNotFoundError:
#     pass
# else:
#     pass

# finally:
#     print("Fayl baghlandi!")
#     file_stream.close()



# raise
# def make_discout(price, discout):
#     if discout > price:
#         raise ValueError("Endirimli qiymet malin oz qiymetinden kichik ola bilmez..")
#     return price - discout


# assert
def make_discout(price, discout):
    assert price > discout, "Endirimli qiymet malin oz qiymetinden kichik ola bilmez.."
    return price - discout



print(make_discout(100, 101))



