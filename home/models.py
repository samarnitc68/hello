from django.db import models

# Create your models here.
class employee_details(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    department = models.CharField(max_length=100)

class department_detals(models.Model):
    dept_id = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=100)

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    body_text = models.DateField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    def __str__(self) -> str:
        return self.headline
# end of program