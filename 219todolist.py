# Create a to do list class that can have categories and items within the categories
# Items can belong to multiple categories.
# Be able to view the intersection of two categories.

class todo_list:
	# Initialise with a set of categories first.
	def __init__(self):
		self.todolist = {}

	# Add an item using this method. First argument is the item whereas subsequent ones are categories
	def addItem(self, *args):
		arguments = [arg for arg in args]
		item = arguments[0]
		categories = arguments[1:]

		for category in categories:
			if category not in self.todolist.keys():
				self.todolist[category] = []
			self.todolist[category].append(item)

	# View the list given a category or list of categories
	def viewList(self, *args):
		list_of_categories = [arg for arg in args]
		category_items = map(lambda x: set(self.todolist[x]), list_of_categories)
		category_intersect = set.intersection(*category_items)

		print('----', ' & '.join(list_of_categories).upper(), '----')
		for item in category_intersect:
			print('-', item)

	# Update an item that is reflected on all categories
	def updateItem(self, old, new):
		for key, val in self.todolist.items():
			for i in range(len(self.todolist[key])):
				if self.todolist[key][i] == old:
					self.todolist[key][i] = new

if __name__ == "__main__":
	test_list = todo_list()
	test_list.addItem("Pet Fido", "Pets")
	test_list.addItem("Send cash to mum", "Chores")
	test_list.addItem("Buy dog food", "Pets", "Chores")

	test_list.viewList("Pets")
	test_list.viewList("Chores")
	test_list.viewList("Pets","Chores")

	test_list.updateItem("Buy dog food", "Buy cat food")
	test_list.viewList("Pets")
	test_list.viewList("Chores")




		


