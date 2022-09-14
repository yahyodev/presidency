from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from .utils import unique_slug_generator
from .validators import validate_rating


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LevelChoices(models.TextChoices):
    beginner = 'Beginner', 'Beginner'
    elementary = 'Elementary', 'Elementary'
    pre_intermediate = 'Pre-Intermediate', 'Pre-Intermediate'
    intermediate = 'Intermediate', 'Intermediate'
    upper_intermediate = 'Upper-Intermediate', 'Upper-Intermediate'
    advanced = 'Advanced', 'Advanced'


class File(models.Model):
    name = models.CharField(max_length=512)
    file = models.FileField(upload_to='files/')


class Category(BaseModel):
    title = models.CharField('title', max_length=256)
    slug = models.SlugField('slug', max_length=256, unique=True)

    def clean(self):
        self.slug = unique_slug_generator(self.__class__, self)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Lesson(BaseModel):
    title = models.CharField('title', max_length=256)
    slug = models.SlugField('slug', max_length=256, unique=True)
    content = RichTextUploadingField('content')
    level = models.CharField('level', max_length=64, choices=LevelChoices.choices)
    category = models.ManyToManyField(Category, verbose_name='category', null=True, blank=True)
    files = models.ManyToManyField('File', null=True, blank=True, verbose_name='files')

    def clean(self):
        self.slug = unique_slug_generator(self.__class__, self)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'lesson'
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Post(BaseModel):
    title = models.CharField('title', max_length=256)
    slug = models.SlugField('slug', max_length=256, unique=True)
    content = RichTextUploadingField('content')
    category = models.ManyToManyField(Category, verbose_name='category', null=True, blank=True)
    views = models.PositiveIntegerField('views')

    def clean(self):
        self.slug = unique_slug_generator(self.__class__, self)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Review(BaseModel):
    full_name = models.CharField('full_name', max_length=256)
    image = models.ImageField('image', upload_to='images/')
    content = models.TextField('content')
    rating = models.PositiveSmallIntegerField('rating', validators=[validate_rating])

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class SocialAccount(BaseModel):
    icon = models.ImageField('icon', upload_to='icons/')
    url = models.URLField('url')

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'social_account'
        verbose_name = 'Social Account'
        verbose_name_plural = 'Social Accounts'


class Contact(BaseModel):
    full_name = models.CharField('full_name', max_length=256)
    email = models.EmailField('email')
    message = models.TextField('message')

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Home(BaseModel):
    full_name = models.CharField('full_name', max_length=256)
    bio = RichTextField('bio')

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'home'
        verbose_name = 'Home'
        verbose_name_plural = 'Home'


class Subscription(BaseModel):
    email = models.EmailField('email')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'subscription'
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
