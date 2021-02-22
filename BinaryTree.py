class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def addchild(self, val):
        if self.data == val:
		# no duplicates
            return

        if self.data > val:
		# adding in left subtree
            if self.left:
                self.left.addchild(val)
            else:
                self.left = BinarySearchTree(val)
        else:
		# adding in right subtree
            if self.right:
                self.right.addchild(val)
            else:
                self.right = BinarySearchTree(val)
	
    def find_min(self):
	if self.left is None:
	    return self.data
	else:
	    return self.left.find_min() 

    def find_max(self):
	if self.right is None:
	    return self.data
	else:
	    return self.right.find_max()


    # in_order will return sorted elements
    def in_order_traversal(self):

        elements = []
	# going through left tree
        if self.left:
            elements += self.left.in_order_traversal()
	
	# going through node
        elements.append(self.data)

	# going through right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
	
    def delete_item(self,val):
	if val < self.data:
	    if self.left:
		self.left.delete_item(val)
	elif val> self.data:
	    if self.right:
		self.right.delete_item(val)

	else:
	    if self.left is None and self.right is None:
		return None
	    if self.right is None:
		return self.right
	    if self.left is None:
		return self.left
	
	    min_val = self.right.find_min()
	    self.data = min_val
	    self.right = self.right.delete(min_val)

	return self

		  

		
    

    # searching for an element
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


if __name__ == "__main__":
    numbers = [17, 11, 2, 3, 4, 8, 9, 10, 22]
    b = BinarySearchTree(12)
    for v in numbers:
        b.addchild(v)
        print("done")

    ele = b.in_order_traversal()
    print(ele)
    print(b.search(200))
