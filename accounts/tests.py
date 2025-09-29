from django.contrib.auth import get_user_model
from django.test import TestCase


class UserManagesTests(TestCase):
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'testsuper',
            email = 'testsuper@gmail.com',
            password = '1234'
		)
        self.assertEqual(admin_user.username, 'testsuper')
        self.assertEqual(admin_user.email, 'testsuper@gmail.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)

        
    def test_cretae_user(self):
        User = get_user_model()
        user = User.objects.create (
            username = 'testuser',
            email = 'testmail@gmail.com',
            password = 'test'
		)
      
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testmail@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
	
