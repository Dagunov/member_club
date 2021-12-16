from datetime import date

members = []

def add_member(member):
	members.append(member)

def email_unique(email):
	for member in members:
		if email == member.email:
			return False
	return True

class Member:
	def __init__(self, name, email) -> None:
		self.id = len(members)+1
		self.name = name
		self.email = email
		self.date = date.today
