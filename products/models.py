from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children',
                                on_delete=models.CASCADE,
                                null=True, blank=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text='You can leave it blank')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'categories'

    def __str__(self):                           
        full_path = [self.title]             
        parent_name = self.parent
        while parent_name is not None:
            full_path.append(parent_name.title)
            parent_name = parent_name.parent
        return ' -> '.join(full_path[::-1])