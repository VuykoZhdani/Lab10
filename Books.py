class Books:
    def __init__(self,author,editor,name,price,publishYear):
        self.author=author
        self.editor = editor
        self.name = name
        self.price = price
        self.publishYear = publishYear
    def __str__(self):
        return f"{self.author}\n {self.editor}\n {self.name}\n  {self.price}\n {self.publishYear} "
