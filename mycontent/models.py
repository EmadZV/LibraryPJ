from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Count
from django.urls import reverse
from django.utils.text import slugify
# from myshop.models import Price
import myauth.models


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True)
    mytranslator = models.ManyToManyField('myauth.Translator',)
    cover = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    description = models.TextField()
    author = models.ManyToManyField('myauth.Author',)
    publisher = models.ForeignKey('myauth.Publisher', on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField('myauth.Category',)
    active = models.BooleanField(default=True)
    file = models.FileField(upload_to='filamoon/', null=True)
    stars = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    price = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('mycontent:book',
                       args=[self.slug])

    @property
    def get_similar_books(self):
        book_tags_ids = self.category.values_list('id', flat=True)
        similar_books = Book.objects.filter(tag__in=book_tags_ids).exclude(id=self.id).distinct()
        similar_books = similar_books.annotate(same_tags=Count('tag')).order_by('-same_tags', '-created')
        return similar_books

    def __str__(self):
        return self.title

    def get_book_stars(self):
        book_votes_count = self.votemodel_set.all().count()
        # book_votes =

        return

    def get_price(self):
        return self.price

    def get_comments(self):
        return self.comment_set.all()

    def get_latest(self):
        return Book.objects.all().order_by('created')[0:5]

    def get_most_viewed(self):
        return None

    def get_most_liked(self):
        return None

    def get_most_discounted(self):
        return None


class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey('myauth.MyUser', on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class CustomModelManager(models.Manager):
    def create(self, *args, **kwargs):
        voter, newvote = kwargs.get('voter'), kwargs.get('vote')
        book, author = kwargs['book'], kwargs['author']
        if book:
            myvote = VoteModel.objects.filter(voter=voter, book=book)
        elif author:
            myvote = VoteModel.objects.filter(voter=voter, author=author)
        else:
            myvote = None
        if myvote.exists():
            prevvote = myvote.values_list('vote', flat=True).last()
            if prevvote == newvote:
                myvote.delete()
            elif prevvote != newvote:
                myvote.delete()
                super(CustomModelManager, self).create(*args, **kwargs)
        else:
            super(CustomModelManager, self).create(*args, **kwargs)


class VoteModel(models.Model):
    voter = models.ForeignKey('myauth.MyUser', on_delete=models.CASCADE, related_name='votes', unique=False)
    vote = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(5)])

    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    publisher = models.ForeignKey('myauth.Publisher', null=True, on_delete=models.CASCADE)
    author = models.ForeignKey('myauth.Author', null=True, on_delete=models.CASCADE)

    objects = CustomModelManager()

    def __str__(self):
        return self.voter.username
