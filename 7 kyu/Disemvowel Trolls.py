# https://www.codewars.com/kata/52fba66badcd10859f00097e


def disemvowel(string_: str):
    return ''.join([x for x in string_ if not (x.isalpha() and x.lower() in ['a', 'e', 'i', 'o', 'u'])])


print(disemvowel('#?KiE-euasYsiKuXEoo,oRi  uJBA( >(uIv oaEc$UQo JoiE"eKX\'e'))
