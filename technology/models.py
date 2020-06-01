from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

# Create your models here.
User = settings.AUTH_USER_MODEL

class AllNews(models.Model):
    title = models.CharField(max_length = 1000, unique=True)
    description = models.TextField()
    url = models.CharField(max_length = 200)
    image_url = models.CharField(max_length = 500)
    author = models.CharField(max_length = 50, default = 'Nepal Tech')
    
    dateTimeObj = timezone.now()
    dateStr = dateTimeObj.strftime("%B %d, %Y")
    posted = models.CharField(default = dateStr, max_length=20)
    scrapped = models.DateTimeField(default=timezone.now, verbose_name='Scrapped On')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'All News'
        ordering=['-scrapped']


class TechNews(models.Model):
    title = models.CharField(max_length = 1000, unique=True)
    description = models.TextField()
    url = models.CharField(max_length = 200)
    image_url = models.CharField(max_length = 500)
    author = models.CharField(max_length = 50, default = 'Nepal Tech')
    
    dateTimeObj = timezone.now()
    dateStr = dateTimeObj.strftime("%B %d, %Y")
    posted = models.CharField(default = dateStr, max_length=20)
    scrapped = models.DateTimeField(default=timezone.now, verbose_name='Scrapped On')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tech News'
        ordering=['-scrapped']

class TelcoNews(models.Model):
    title = models.CharField(max_length = 1000, unique=True)
    description = models.TextField()
    url = models.CharField(max_length = 200)
    image_url = models.CharField(max_length = 500)
    author = models.CharField(max_length = 50, default = 'Nepal Tech')
    
    dateTimeObj = timezone.now()
    dateStr = dateTimeObj.strftime("%B %d, %Y")
    posted = models.CharField(default = dateStr, max_length=20)
    scrapped = models.DateTimeField(default=timezone.now, verbose_name='Scrapped On')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Telecom News'
        ordering=['-scrapped']

class GadgetNews(models.Model):
    title = models.CharField(max_length = 1000, unique=True)
    description = models.TextField()
    url = models.CharField(max_length = 200)
    image_url = models.CharField(max_length = 500)
    author = models.CharField(max_length = 50, default = 'Nepal Tech')
    
    dateTimeObj = timezone.now()
    dateStr = dateTimeObj.strftime("%B %d, %Y")
    posted = models.CharField(default = dateStr, max_length=20)
    scrapped = models.DateTimeField(default=timezone.now, verbose_name='Scrapped On')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Gadget News'
        ordering=['-scrapped']

class GlobalNews(models.Model):
    title = models.CharField(max_length = 1000, unique=True)
    description = models.TextField()
    url = models.CharField(max_length = 200)
    image_url = models.CharField(max_length = 500)
    author = models.CharField(max_length = 50, default = 'Nepal Tech')
    
    dateTimeObj = timezone.now()
    dateStr = dateTimeObj.strftime("%B %d, %Y")
    posted = models.CharField(default = dateStr, max_length=20)
    scrapped = models.DateTimeField(default=timezone.now, verbose_name='Scrapped On')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Global Tech News'
        ordering=['-scrapped']

#Creating this NewsPostQuerySet and  NewsPostManager class to display only the published News. The News are visible if
# they are older than now. Future Newss wont be visible in the views
# class NewsPostQuerySet(models.QuerySet):
#     def published(self):
#         now = timezone.now()
#         return self.filter(publish_date__lte = now)

# class NewsPostManager(models.Manager):
#     def get_queryset(self):
#         return NewsPostQuerySet(self.model, using = self._db)
#     def published(self):
#         return self.get_queryset().published()

class NewsPost(models.Model):
    # id = models.IntegerField() #by default with primary key
    #Associating User with a News Post
    user = models.ForeignKey(User, default = 1, null = True, on_delete = models.SET_NULL) #Default = 1, means Superuser
    title = models.CharField(max_length = 120, unique= True, verbose_name = 'Title')
    image = models.ImageField(upload_to = 'editor_news/', blank = True, null = True)
    content = models.TextField(verbose_name = 'Content')
    publish_date = models.DateTimeField(auto_now = False, auto_now_add = False, null = True, blank = True, verbose_name = 'Published On')
    updated = models.DateTimeField(auto_now = True, auto_now_add = False, verbose_name = 'Last Modified')
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True, verbose_name = 'Posted on')
    slug = models.SlugField(max_length = 150)
    

    # These objects are only published objects
    # objects = NewsPostManager()

    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse("detail", kwargs = {'id' : self.id})
    # def get_edit_url(self):
    #     return reverse("edit", kwargs = {'id' : self.id})
    # def get_delete_url(self):
    #     return reverse("delete", kwargs = {'id' : self.id})
    class Meta:
        verbose_name_plural = "Editor News"
        ordering = ['-publish_date', '-updated', '-timestamp']

class Search(models.Model):
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.SET_NULL)
    search = models.CharField(max_length = 256)
    timestamp = models.DateTimeField(auto_now_add = True, verbose_name = "Searched on")

    class Meta:
        verbose_name_plural = "Searches"

