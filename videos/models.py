from django.db import models

# Create your models here.


#class 형태 orm=object relation model
class Video(models.Model):                      #Db에 만들 테이블을 여기다 넣는 것(비디오로 만드는 것)
    title = models.CharField(max_length=120)    #input박스는 CharField를 넣는다.(타이틀 같은 것을 적을 때)
    embed_code = models.TextField()             #많은 스트링 값을 받는 형태(게시판)

    def __str__(self):
        return str(self.title)
    def __unicode__(self):                      #다국어 코드를 지원하기 위해 넣는거라고 생각할 것
        return str(self.title)