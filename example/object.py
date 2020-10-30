raw_asserts = [
    {
        "func": "expectText",
        "path.class": "article-title",
        "expect": "Community Guidelines"
    },
    {
        "func": "exist",
        "path.class": "to-top to-top-enter-done"
    },
    {
        "func": "expectRect",
        "path.class": "to-top to-top-enter-done",
        "rect.width": 150,
        "rect.height": 150
    }
]

locators = {}

for item in raw_asserts:
    locators["locator=" + item["path.class"]] = {
        "type": "WebElement"
    }

print(locators)