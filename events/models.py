from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
import datetime


class Event(models.Model):
    NOW = datetime.datetime.now()
    YEAR = NOW.year
    if NOW.month > 7:
        YEAR += 1

    YEAR_CHOICES = [
        (5000, 'Alle (inkludert alumni)'),
        (YEAR+4, '1. - 5. klasse'),
        (YEAR+3, '2. - 5. klasse'),
        (YEAR+2, '3. - 5. klasse'),
        (YEAR+1, '4. og 5. klasse'),
        (YEAR, '5. klasse')
    ]

    def get_class_year(self, graduation_year):
        return graduation_year - self.YEAR

    title = models.CharField(max_length=200, unique=True)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField()
    location = models.CharField(max_length=50, blank=True, null=True)
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField(blank=True, null=True)
    registration_required = models.BooleanField(default=False)
    registration_start_time = models.DateTimeField(blank=True, null=True)
    alumni = models.BooleanField(default=False)
    class_1 = models.BooleanField(default=False)
    class_2 = models.BooleanField(default=False)
    class_3 = models.BooleanField(default=False)
    class_4 = models.BooleanField(default=False)
    class_5 = models.BooleanField(default=False)
    only_komite = models.BooleanField(default=False)
    available_spots = models.IntegerField(blank=True, null=True)
    registered_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='registerd_users')
    waiting_list = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='waiting_list_users')
    slug = models.SlugField(max_length=60, blank=True)
    image = ProcessedImageField(upload_to='events/', processors=[ResizeToFit(2000, 2000, False)], format='JPEG',
                                options={'quality': 85})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Only set the slug when the object is created.
            self.slug = slugify(self.title)  # Or whatever you want the slug to use
        if not self.registration_start_time:
            self.registration_start_time = self.event_start_time
        super(Event, self).save(*args, **kwargs)

    def is_now(self, month):
        if month == datetime.datetime.now().month:
            return True
        else:
            return True

    class Meta:
        # ordering = ['event_start_date']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['event_start_time', 'title']