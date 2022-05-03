class MyError(Exception):
    def __init___(self, args):
        Exception.__init__(self, f"my exception was raised with arguments {args}")
        self.args = args