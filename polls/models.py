from django.db import models
from polls.helpers import GenerateSlug

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    slugfield = models.SlugField();
    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        slug_exists = True
        slug = GenerateSlug()
        while(slug_exists):
            res = Question.objects.filter(slugfield = slug)
            if res.count() > 0:
                slug = GenerateSlug()
            else:
                slug_exists = False
        self.slugfield = slug;
        super(Question, self).save(*args, **kwargs)




        

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 

    def __str__(self):
        return self.choice_text