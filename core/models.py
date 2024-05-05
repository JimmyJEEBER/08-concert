from django.db import models

# Create your models here.
class Artists(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=128)
    genres = models.CharField(max_length=256, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.artist_name
    
class Songs(models.Model):
    song_id = models.IntegerField(primary_key=True)
    song_name = models.CharField(max_length=256)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name='songs')
    duration = models.IntegerField()
    release_date = models.DateField()

class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Concert(models.Model):
    concert_id = models.AutoField(primary_key=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.artist} at {self.venue} on {self.date_time}"
    

