from django.test import TestCase , Client
from bs4 import BeautifulSoup
from .models import Post


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        #1.1 포스트 목록 페이지 가져오기
        response =self.client.get('/blog')
        #1.2 정상적으로 페이지가 로드되기
        self.assertEqual(response.status_code, 200)
        #1.3 페이지 타이틀은 'blog'이다
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text,'Blog')
        #1.4 내비게이션 바가 이싿
        navbar = soup.nav
        #1.5 blog, about me 라는 문구가 네비게이션바에 있다
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)
        #2.1 메인 영역에 게시물이 하나도 없다면
        self.assertEqual(Post.objects.count(),0)
        # 2.2 아직 게시물이 없습니다.    라는 문구가 보인다
        main_area=soup.find('div',id='main-area')
        self.assertIn('아직 게시물이 없습니다.',main_area.text)
        #3.1 게시물이 2개있다면
        post_001=Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. we are the world',

        )
        post_002 = Post.objects.create(
            title= '두번째 포스트입니다.',
            content='1등이 전부는 아니잖아 '
        )
        self.assertEqual(Post.objects.count(),2)

        #3.2 포스트 목록 페이지를 새로고침했을때
        reponse= self.client.get('/blog/')
        soup= BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code,200)

        #3.3 메인 영역에 포스트 2개의 타이틀이 존재한다
        main_area=soup.find('div',id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        #3.4 아직 게시물이 ㅇ벗습니다. 라는 문가 더이상 보이지 않는다
        self.assertIn('아직게시물이없습니다.',main_area.text)
