from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

LANGUAGES = (
    (u'tr', u'Turkish'),
    (u'en', u'English'),
)


class Post(models.Model):
    """Base model for blog posts."""

    author = models.ForeignKey(User)
    status = models.BooleanField('Active', default=False)
    archive = models.BooleanField(default=False)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='tr')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    pub_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        ordering = ['-pub_date']

    @property
    def is_active(self):
        return self.status

    def get_absolute_url(self):
        return '/{:s}/'.format(self.slug)

    def save(self, *args, **kwargs):
        if not self.id:
            self.pub_date = datetime.now()
        self.update_date = datetime.now()
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
