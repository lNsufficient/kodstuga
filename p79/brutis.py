import csv
from itertools import chain
import random

with open('keylog.txt', 'r') as f:
    keys = [l[0] for l in csv.reader(f)]

def make_smaller_constraints(key):
    return key[:2], key[1:], key[0] + key[2]

keys = list(chain(*[make_smaller_constraints(key) for key in keys]))
print(keys)

print(len(keys))
keys = sorted(list(set(keys)))
print(len(keys))

print(keys)

if 0:
    k = []
    for n in keys:
        if n[0] != '7' and n[-1] != '0':
            k.append(n)
    print(k)
    exit()


if 0:
    def check_if_key_works_with_insert(password, key):
        is_working = False
        if key[0] not in password and key[1] not in password:
            password += key
            is_working = True
        elif key[0] not in password:
            k = password.index(key[1])
            password = password[:k] + key[0] + password[k:]
            is_working = True
        elif key[1] not in password:
            n = password[::-1].index(key[0])
            password = password[:n] + key[1] + password[n:]
            is_working = True
        else:
            k = password.index(key[0])
            n = password[::-1].index(key[1])
            n = len(password) - 1 - n
            is_working = k < n

        return password, is_working


    password = keys[0]
    for key in keys[1:]:
        print(password)
        password, is_working = check_if_key_works_with_insert(password, key)
        if not is_working:
            print('failed on {} using key {}'.format(password, key))


def check_if_key_works(password, key):
    is_working = False
    if key[0] not in password or key[1] not in password:
        is_working = False
    else:
        k = password.index(key[0])
        n = password[::-1].index(key[1])
        n = len(password) - 1 - n
        is_working = k < n

    return is_working

attempts = 0


while True:
    attempts += 1
    r = random.randint(0, 99999999)
    password = '{:08d}'.format(r)
    #password = '73162890'
    #print('pass:', password)
    for key in keys:
        is_working = check_if_key_works(password, key)
        if not is_working:
            break
        #else:
            #print(key)
    else:
        print('Done!', password, 'attempts', attempts)
        break
