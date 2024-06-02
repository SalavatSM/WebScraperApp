from django.db import models


class ScrapedData(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()
    date_scraped = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
