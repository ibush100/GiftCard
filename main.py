import find_gift
import parse_file


def test_zero_balance():
    items = parse_file.open_and_format('find-pair prices.txt')
    assert find_gift.search(items, 2500) == ('Candy Bar', 'Earmuffs')


def test_low_balance():
    items = parse_file.open_and_format('find-pair prices.txt')
    assert find_gift.search(items, 4000) == ('Headphones', 'Earmuffs')


def test_no_budget():
    items = parse_file.open_and_format('find-pair prices.txt')
    assert find_gift.search(items, 0) == 'no gift found'


if __name__ == '__main__':
    test_zero_balance()
    test_low_balance()
    test_no_budget()





