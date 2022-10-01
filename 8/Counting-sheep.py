# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python


def count_sheeps(sheep):
    return len(list(filter(lambda x: x is True, sheep)))


print(count_sheeps([True, True, True, False,
              True, True, True, True,
              True, False, True, False,
              True, False, False, True,
              True, True, True, True,
              False, False, True, True]))
