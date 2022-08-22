# Implementing linked list
# Creating a linked list
class Node:
	def __init__(self, dataval=None):
		self.dataval = dataval
		self.nextval = None
class SLinkedList:
	def __init__(self):
		self.headval = None

	def listprint(self):
		printval = self.headval
		while printval is not None:
			print (printval.dataval)
			printval = printval.nextval

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Linking the first node to second node
list1.headval.nextval = e2

# Linking the seconfd node to third node
e2.nextval = e3

list.listprint()