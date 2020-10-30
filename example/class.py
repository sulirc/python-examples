# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print('Parent')

#     def bar(self, message):
#         print("%s from Parent" % message)


# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
#         super(FooChild, self).__init__()
#         print('Child')

#     def bar(self, message):
#         super(FooChild, self).bar(message)
#         print('Child bar fuction')
#         print(self.parent)


# fooChild = FooChild()
# fooChild.bar('HelloWorld')

class Window:
  def __init__(self, name):
    self.name = name
    print("window name = {}".format(name))

  def print_fancy_name(self):
    print("Fancy window name: {}".format(self.name))


class WebviewWindow(Window):
  # def __init__(self, name, size):
  #   super(WebviewWindow, self).__init__(name)
  #   self.size = size
  #   print("window size = {}".format(size))
  def sigh(self):
    print("Ahhh")

# w = Window("Cat")
# w.print_fancy_name()

ww = WebviewWindow("Dog")
# w.print_fancy_name()