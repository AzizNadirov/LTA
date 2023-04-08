# Fayllar - fayllara yazmaq, icazə modları və with
# r - read; w - write; a - append; x - create
# + - read/write



# file_stream = open('folder/file.txt', 'w')    # yazı modunda

# content = "New line for file\n"

# file_stream.write(content)


# print(file_stream.tell())
# file_stream.seek(0)
# print(file_stream.read())                     # oxumaq olmaz!

# file_stream.close()


# with - contekst menecer
# özu sonda bağlayacaq.
with open('folder/file.txt', mode='r') as file_stream:
    print(file_stream.read())
    file_stream.write('some content')