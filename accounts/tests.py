from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='Adam', 
            email='adam@adam.com',
            password='123abc'
        )
        self.assertEqual(user.username, 'Adam')
        self.assertEqual(user.email, 'adam@adam.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superuser', 
            email='superuser@superuser.com',
            password='123abc'
        )
        self.assertEqual(user.username, 'superuser')
        self.assertEqual(user.email, 'superuser@superuser.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        