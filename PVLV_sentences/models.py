from djongo import models

QUIET_MODE = 1
NORMAL_MODE = 2
SPAM_MODE = 3


class MetaData(models.Model):
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField()
    n_edits = models.IntegerField()
    rating = models.IntegerField()

    class Meta:
        abstract = True


class Author(models.Model):
    name = models.CharField(max_length=100)


class Sentence(models.Model):
    content = models.CharField(max_length=100)
    # added_by =


class Collection(models.Model):
    name = models.CharField(max_length=100)


class Container(models.Model):
    title = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)
    mode = models.IntegerField(default=QUIET_MODE)
    private = models.BooleanField(default=False) # if is private you have to check the authorization group
    authorization_group = None

    authors = models.OneToOneField(
        to=Author,
        on_delete=models.CASCADE,
    )
    date_creation = models.DateTimeField(auto_now_add=True)

    sentences = models.ArrayModelField(
        model_container=Collection,
    )

    created_on_datetime = models.DateField()
    last_edit_datetime = models.DateField()

    def __str__(self):
        return self.title
