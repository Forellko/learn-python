def hello(to, cb):
  print("hello", to)
  cb()
  return 

def callback():
  print('in callback')

name = input("What is your name? ")

hello(name, callback)