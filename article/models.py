from django.db import models
        
class Article(models.Model):
    article_text = models.CharField(max_length=30, blank=True)
    article_creation_date = models.DateField()
    
    def __str__(self):       # <- NEW
        return self.article_text    # <- NEW