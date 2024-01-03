from util import Receipt

class prompter(object):
    def __init__(self):
        self.receipt = Receipt()
        self.welcome = "Welcome to Splease, a bill splitting app!"

    # method that greets the user and asks what they wanna do next
    def begin(self):
        print(self.welcome)
