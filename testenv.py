from __future__ import print_function
import os
import sys

DEBUG = os.environ.get('DEBUG') == 'true'

try:
    import dataset
except:
    if DEBUG:
        raise
    print("Failed to import dataset")
    sys.exit(1)

try:
    import mechanize
except:
    if DEBUG:
        raise
    print("Failed to import mechanize")
    sys.exit(1)

try:
    import pyquery
except:
    if DEBUG:
        raise
    print("Failed to import pyquery")
    sys.exit(1)

try:
    import requests
except:
    if DEBUG:
        raise
    print("Failed to import requests")
    sys.exit(1)


def run_test(name, callee):
    print("Testing %s... " % name, end="")
    try:
        callee()
    except:
        print("FAIL")
        if DEBUG:
            raise
        sys.exit(1)
    else:
        print("OK")


def test_dataset():
    db = dataset.connect('sqlite:///:memory:')

    table = db['sometable']
    table.insert(dict(name='John Doe', age=37))
    table.insert(dict(name='Jane Doe', age=34, gender='female'))

    john = table.find_one(name='John Doe')


def test_mechanize():
    br = mechanize.Browser()
    br.open("http://example.com")
    br.title()


def test_pyquery():
    d = pyquery.PyQuery("<html><body><p class='test'>Hello!</p></body></html>")
    d('p.test').text()


def test_requests():
    res = requests.get("http://example.com")
    res.raise_for_status()


def main():
    run_test('dataset', test_dataset)
    run_test('mechanize', test_mechanize)
    run_test('pyquery', test_pyquery)
    run_test('requests', test_requests)

    print("Hooray! It looks like everything worked.")


if __name__ == '__main__':
    main()
