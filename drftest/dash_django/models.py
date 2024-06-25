from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Character(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    # ~ We could use this for the CreatedOn field
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 30)
    strength = models.IntegerField(
        default = 10,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ]
    )
    agility = models.IntegerField(
        default = 10,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ]
    )
    intelligence = models.IntegerField(
        default = 10,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ]
    )
    
    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)