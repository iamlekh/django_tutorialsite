from django.db import models
from datetime import datetime


class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)
# 
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category





class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory,verbose_name="Category",on_delete = models.CASCADE)
    series_summary = models.CharField(max_length=200)

    class Meta:
        #Otherwise we get "Tutorial Serie*ss* in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
        tutorial_title = models.CharField(max_length=200)
        tutorial_content = models.TextField()
        tutorial_published = models.DateTimeField("date published", default = datetime.now())
        tutorial_series = models.ForeignKey(TutorialSeries, verbose_name="Series", blank=True, null=True,on_delete = models.CASCADE) #<--changes
        tutorial_slug = models.CharField(max_length=200,default=1)

        def __str__(self):
            return self.tutorial_title
