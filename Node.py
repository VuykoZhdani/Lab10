from Include.Books import Books

Books


class Node:
    print("Hello")
    print("Hello")

    def __init__(self, name, left=None, right=None):
        print("Hello")
        self.left = left
        self.right = right
        self.name = name
        print("Hello")

        def deleteNodeByAuthor(self, author):
            if self is None:
                return
            if author < self.author:
                self.left = deleteNodeByAuthor(self.left, author)
            elif author > self.author:
                self.right = deleteNodeByAuthor(self.right, author)
            else:
                if self.left is None and self.right is None:
                    return None
                elif self.left and self.right:
                    predecessors = self.findMaximumKey(self.left)
                    self.author = predecessors.author
                    self.left = deleteNodeByAuthor(self.left, predecessors.author)
                else:
                    child = self.left if self.left else self.right
                    self = child
            return self
            print("Hello")

    def postorder(self, editor):
        if self.left is not None:
            self.left.postorder(editor)
        if self.right is not None:
            self.right.postorder(editor)
        if self.editor is not None:
            editor.append(self.editor)
        return editor
        print(Hello)
