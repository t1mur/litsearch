class Paper:
	def __init__(self, species, URL, author, year):
		self.species=species
		self.author=author
		self.URL=url
		self.year=year
	def __init__(self, allInOneArray):
		self.species=allInOneArray[0]
		self.author=allInOneArray[1]
		self.URL=allInOneArray[2]
		self.year=allInOneArray[3]
testInstance=Paper(["1","2","3","4"])
print(testInstance.URL)