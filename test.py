import multiprocessing
from hashlib import md5


def generator_str(x, password='', start=0, end=0):
    if len(password) == 6:
        yield password
    else:
        if len(password) == 0:
            m = x[start:end]
        else:
            m = x
        for i in m:
            new_password = password + i
            yield from generator_str(x=x, password=new_password)

def start_x(x, start, end):
    hash_list = ['3bd0a32f99a0185c8a8f4af9ccff90ae',
'8bad66e16b191a1f779f4c9f9f0955ea',
'6467b3d4f0176029b582280342c83d33']
    for i in generator_str(x=x, start=start, end=end):
        password_hash = md5(i.encode()).hexdigest()
        if password_hash in hash_list:
            print(i, password_hash)


# x = md5(('maythe' + ' ' + '4th0be' + ' ' + 'with0u').encode()).hexdigest()
# print(x == '0fa4942803ffbdb8dec14548f06f50cf')

if __name__ == '__main__':
    x = [chr(97 + i) for i in range(26)]
    x.extend([chr(48 + i) for i in range(10)])
    print(len(x))
    process1 = multiprocessing.Process(target=start_x, args=(x, 0, 6))
    process2 = multiprocessing.Process(target=start_x, args=(x, 6, 12))
    process3 = multiprocessing.Process(target=start_x, args=(x, 12, 18))
    process4 = multiprocessing.Process(target=start_x, args=(x, 18, 24))
    process5 = multiprocessing.Process(target=start_x, args=(x, 24, 30))
    process6 = multiprocessing.Process(target=start_x, args=(x, 30, 37))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()


