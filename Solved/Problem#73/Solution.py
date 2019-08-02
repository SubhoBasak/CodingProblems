class data_map:
	def __init__(self):
		self.records = {}

	def set(self, key, value, time):
		if key in self.records:
			if type(self.records[key]) != dict:
				self.records[key] = {}
			self.records[key][time] = value
		else:
			self.records[key] = {}
			self.records[key][time] = value

	def get(self, key, time):
		tmp_lst = list(self.records[key].keys())
		tmp_lst.sort()
		if time < tmp_lst[0]:
			return None
		cur = tmp_lst[0]
		for i in tmp_lst[1:]:
			if i < time:
				cur = i
			else:
				break
		return self.records[key][cur]


d = data_map()

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
print(d.get(1, 1)) # get key 1 at time 1 should be 1
print(d.get(1, 3)) # get key 1 at time 3 should be 2

d = data_map()

d.set(1, 1, 5) # set key 1 to value 1 at time 5
print(d.get(1, 0)) # get key 1 at time 0 should be null
print(d.get(1, 10)) # get key 1 at time 10 should be 1

d = data_map()

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
print(d.get(1, 0)) # get key 1 at time 0 should be 2
