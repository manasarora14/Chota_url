import string

BASE62 = string.digits + string.ascii_letters  # 0-9 + A-Z + a-z

def encode_base62(num):
    if num == 0:
        return BASE62[0]
    base62 = []
    while num > 0:
        num, rem = divmod(num, 62)
        base62.append(BASE62[rem])
    return ''.join(reversed(base62))
