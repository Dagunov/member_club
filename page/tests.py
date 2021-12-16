from django.test import TestCase, RequestFactory

from .models import Member, add_member, members

from string import ascii_lowercase
from random import choice

def random_email():
	mail = ''.join([choice(ascii_lowercase) for i in range(10)])
	return mail + '@gmail.com'

def random_name():
	return ''.join([choice(ascii_lowercase) for i in range(10)])


class PageTestCase(TestCase):
	def test_add_member(self):
		# [SCENARIO] When new member is added, he should be added in a table on the page

		# [GIVEN] Index view
		from .views import index

		# [GIVEN] New member information
		email = random_email()
		name = random_name()

		# [GIVEN] Member
		member = Member(name, email)

		# [WHEN] Member is added
		add_member(member)

		# [THEN] Page should be rendered without an error
		request = RequestFactory().get('')
		response = index(request)

		# [THEN] Member must be present in the table
		user = ('<tr><td>{}</td><td>{}</td><td>{}</td>').format(member.id, member.name, member.email)
		self.assertTrue(
			user in response.content.decode().replace('\n', '').replace('\t', ''),
			msg='New member must be in table.')

		# [BREAKDOWN]
		members.clear()

	def test_add_duplicate_email(self):
		# [SCENARIO] If there already is a member with given email, an error must be shown.

		# [GIVEN] Index view
		from .views import index

		# [GIVEN] New member information
		email = random_email()
		name = random_name()

		# [GIVEN] One member added already
		request = RequestFactory().post(
			'',
			{'name': name, 'email': email})
		index(request)

		# [WHEN] Adding the same member again
		request = RequestFactory().post(
			'',
			{'name': name, 'email': email})
		response = index(request)

		# [THEN] An error must be shown
		error = '<ul class="errorlist"><li>There already is a member with this email</li></ul>'
		self.assertTrue(
			error in response.content.decode().replace('\n', '').replace('\t', ''), 
			msg='An error must be shown.')

		# [THEN] Only one member should be added
		self.assertEqual(len(members), 1,
			msg='Only one member should be added.')

		# [BREAKDOWN]
		members.clear()
