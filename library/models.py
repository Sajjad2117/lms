from django.db import models


class Library(models.Model):
    library_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.library_name}'


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000, default="About book")
    author = models.CharField(max_length=100)
    library_name = models.ForeignKey(Library, on_delete=models.CASCADE)
    major_name = models.ForeignKey(Major, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_rating = models.IntegerField(default=0)
    date_rent = models.DateTimeField()

    image = models.ImageField(
        default='default_book.png', upload_to='books_pics')

    def __str__(self):
        return self.title
