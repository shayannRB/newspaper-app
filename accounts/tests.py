from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


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

class SignUpPageView(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)	

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))	
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response = self.client.post(
            reverse('signup'),
            {
                "username" : 'testuser',
                'email' : 'testmail@gmail.com',
                'password1' : 'testpass',
                'password2' : 'testpass'          
            }
        )
        self.assertEqual(response.status_code, 200)							         
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')							         
        self.assertEqual(get_user_model().objects.all().counts(), 1)							         
        self.assertEqual(get_user_model().objects.all()[0].email, 'testmail@gmail.com')							         