from django.db import models
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    named_url = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=300, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return '#'
        return self.url or '#'

    def __str__(self):
        return self.title