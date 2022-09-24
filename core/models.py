from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from .utils import unique_slug_generator
from .validators import validate_rating
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.core.mail import send_mail, get_connection
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LevelChoices(models.TextChoices):
    all = 'All', 'All'
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


class Type(BaseModel):
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField('title', max_length=256)
    slug = models.SlugField('slug', max_length=256, unique=True)
    order = models.PositiveSmallIntegerField('order')

    class Meta:
        db_table = 'type'
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def clean(self):
        self.slug = unique_slug_generator(self.__class__, self)

        if self.parent and self.parent.parent:
            raise ValidationError('You can not create sub-sub-type')

        if self.parent is None and Type.objects.filter(parent=None).count() >= 6:
            raise ValidationError("You can not add more types without a parent")


class Lesson(BaseModel):
    title = models.CharField('title', max_length=256)
    thumbnail = models.ImageField('image', upload_to='images/')
    description = models.CharField('description', max_length=512)
    slug = models.SlugField('slug', max_length=256, unique=True)
    content = RichTextUploadingField('content')
    level = models.CharField('level', max_length=64, choices=LevelChoices.choices, default='All')
    category = models.ManyToManyField(Category, verbose_name='category', null=True, blank=True)
    type = models.ForeignKey('Type', verbose_name='type', on_delete=models.PROTECT)
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
    thumbnail = models.ImageField('image', upload_to='images/')
    description = models.CharField('description', max_length=512)
    slug = models.SlugField('slug', max_length=256, unique=True)
    content = RichTextUploadingField('content')
    category = models.ManyToManyField(Category, verbose_name='category', null=True, blank=True)

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
    icon = models.FileField('icon', upload_to='icons/', validators=[FileExtensionValidator(['svg', 'png'])],
                            help_text='only .svg and .png files can be uploaded')
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

    @staticmethod
    def get_solo():
        return Home.objects.get_or_create()[0]


class Subscription(BaseModel):
    email = models.EmailField('email', unique=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'subscription'
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'


class MailToSubscribers(BaseModel):
    title = models.CharField('title', max_length=256)
    content = RichTextUploadingField('content')


@receiver(post_save, sender=MailToSubscribers)
def send_msg(sender, instance, created, **kwargs):
    if created:
        subject = instance.title
        message = instance.content
        email_from = settings.EMAIL_HOST_USER
        recipient_list = list(Subscription.objects.values_list('email', flat=True))
        send_mail(subject=subject, html_message=message, message=None, from_email=email_from,
                  recipient_list=recipient_list, )
