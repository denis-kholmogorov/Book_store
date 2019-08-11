from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Will",
            email='Pupkin@waw.ty',
            password='123456789'
        )
        self.assertEqual(user.username, 'Will')
        self.assertEqual(user.email, 'Pupkin@waw.ty')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="admin",
            email='admin@waw.ty',
            password='123456789'
        )
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@waw.ty')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
