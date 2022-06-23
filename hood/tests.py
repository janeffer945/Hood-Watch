from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='david')
        self.post = Post.objects.create(id=1, title='post one', content='api content',image='search?q=mercedes&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjj-7jeyaz4AhUY04UKHb8cAnMQ_AUoAXoECAMQAw&biw=1294&bih=636&dpr=1',
        author=self.user, link='http://search?q=mercedes&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjj-7jeyaz4AhUY04UKHb8cAnMQ_AUoAXoECAMQAw&biw=1294&bih=636&dpr=1')
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)