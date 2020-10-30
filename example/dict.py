assert_dict = {}


def assert_visible():
    print("I am visible")


def assert_rect():
    print("I am rect")


assert_dict['visible'] = assert_visible
assert_dict['rect'] = assert_rect

keys = assert_dict.keys()

if "rect" in keys:
    print("rect in keys")
