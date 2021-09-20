import unittest
from app.models import Pitch
Pitch = Pitch

class PitchTest(unittest.TestCase):

    def setUp(self):

        self.new_pitch = Pitch(category="Innovative", content="Hi")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.content,"Hi")
        self.assertEquals(self.new_pitch.category,"Innovative")        