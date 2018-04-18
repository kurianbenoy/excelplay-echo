from django.test import TestCase
from core.models import Echouser,EchoUserSubmission

class ModelTests(TestCase):
	def setup(self):
		Echouser.objects.create(userid=13,points=0,rank=100)
		Echouser.objects.create(userid=100,points=10,rank=90)
		Echouser.objects.create(userid=1,points=50,rank=40)

