import unittest
from app.models import Comment, Pitch
from app import db

class TestPitchComment(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(content = "A ship that uses controlled explosions", category='Innovative')
        self.new_comment = Comment(comment = "Interesting", pitch=self.new_pitch)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,"Interesting")
        self.assertEquals(self.new_comment.pitch,self.new_pitch,"A ship that uses controlled explosions")