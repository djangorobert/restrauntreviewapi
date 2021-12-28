from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Restraunt(models.Model):
    NEWMEXICO = 'NM'
    TEXAS = 'TX'

    STATE = [
        (NEWMEXICO, 'NM'),
        (TEXAS, 'TX'),


    ]

    name = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=12,
                             choices=STATE,
                             default=NEWMEXICO,)
    post_date = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restraunt, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })


class Reviews(models.Model):

    ONE = 'one'
    TWO = 'two'
    THREE = 'three'
    FOUR = 'four'
    FIVE = 'five'

    RATINGS = [
        (ONE, 'one'),
        (TWO, 'two'),
        (THREE, 'three'),
        (FOUR, 'four'),
        (FIVE, 'five'),
    ]
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    restraunt = models.ForeignKey(Restraunt, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=12,
                              choices=RATINGS,
                              default=THREE,
                              )
    comment = models.TextField(max_length=300)

    def __str__(self):
        return str('%s %s' % (self.restraunt, self.comment))
