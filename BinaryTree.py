import Books
from Include.Node import Node
Node
class Tree:
    def main(self):
        book1=Books("Batman","Joker","chmo",100,2000)
        book2 = Books("chmo", "Batman", "Joker", 100, 2000)
        book3 = Books("mraz", "Ace", "Sky", 100, 2000)
        new_binary_tree=Books()
        new_binary_tree.insertByName(book1)
        new_binary_tree.insertByName(book2)
        new_binary_tree.insertByName(book3)
        new_binary_tree.deleteNodeByAuthor()
        new_binary_tree.postorder()

