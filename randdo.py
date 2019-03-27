import random


def get_random_number():
    i = random.randint(1,1000)
    return i


def get_random_words(length):  # start function, take    length
    all_t = get_text()  # all text = peredannui text
    all_list = all_t.split()  # ves text radelit po probelam
    sample = random.sample(all_list, length)  # присвоим переменной семпл рандомные значения из списка количеством - ленгхт
    istr = ' '.join(str(x) for x in sample)
    return istr  # vernut' peremennuг


get_random_words(length=random.randint(10,20))

length = random.sample ([10,11,12,13,14,15,16,17,18,19,20] 1)
def get_text():
    text = "Cookies: Cookies are pieces of information stored " \
               "directly on the computer that you are using. Cookies " \
               "allow us to collect information such as browser type, " \
               "time spent on the Digital Services, pages visited, " \
               "language preferences, and other web traffic data. " \
               "We, and our service providers, use the information " \
               "for security purposes, to facilitate online navigation, " \
               "to display information more effectively, to personalize your " \
               "experience while using the Digital Services, and to otherwise " \
               "analyze user activity. We can recognize your computer to assist " \
               "your use of the Digital Services. We also gather statistical " \
               "information about the usage of the Digital Services in order " \
               "to continually improve their design and functionality, " \
               "understand how the Digital Services are used, and assist us " \
               "with resolving questions regarding the Digital Services. " \
               "Cookies further allow us to select which of our offers are most " \
               "likely to appeal to you and to display them to you. We may also " \
               "use cookies to see how you interact with our offers, and we may use " \
               "cookies or other files to understand your use of our websites."
    return text