#QR Code
# use the local machine to execute the code, rather than online IDE
import qrcode

qr = qrcode.QRCode(version = 1, box_size = 1, border = 2)
data = '''India is my motherland country where I took birth. I love India and have proud of it. India is a big democratic country that ranks second in population after China. It has a rich and glorious past. It is considered the country of old civilization in the world. It is a land of learning where students from many corners come to study in the big universities.

It is famous for its various unique and diverse cultures and tradition of people of many religions. Some people abroad as well follow Indian culture and tradition because of being attracted to nature. Various invaders came and steal the glory and precious things of India. Some of them made it a slave country; however various great leaders of the country became successful in making my motherland free of Britishers in 1947.

The day our country got freedom means the 15th of August is celebrated every year as Independence Day. Pt. Nehru became the first prime minister of India. It is a country rich in natural resources, yet the inhabitants here are poor. It is growing continuously in technology, science, and literature because of eminent people like Rabindra Nath Tagore, Sir Jagdish Chandra Bose, Sir C.V.Raman, Shri H. N. Bhabha, etc. It is a peace-loving country where people of many religions follow their own culture and tradition as well as celebrate their festivals without any interference.

There are many glorious historical buildings, heritages, monuments and sceneries which attract people mind from different countries every year. Taj Mahal is a great monument in India and a symbol of eternal love and Kashmir as the heaven on the earth. It is a country of famous temples, mosques, churches, Gurudwaras, rivers, valleys, fertile plains, highest mountain, etc.'''

# the above summary can be read from a .txt file aswell, to keep it more simple a (.txt) file is not used here
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = 'red', back_color = 'white')


img.save('destination path') # replace the string with actual destination path