import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models
from django.urls import reverse

class Migration(migrations.Migration):

 initial = True
dependencies = [
  migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

operations = [
 migrations.CreateModel(
  name='Post',
  fields=[
 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
 ('title', models.CharField(max_length=100)),
 ('content', models.TextField()),
 ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
 ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
('first_name', models.CharField(max_length=30)),
 ('surnname', models.CharField(max_length=30)),
 ('Email', models.CharField(max_length=100)),
 ('ADDRESS_1', models.CharField(max_length=30)),
 ('ADDRESS_2', models.CharField(max_length=30)),
 ('ADDRESS_3', models.CharField(max_length=30)),
 ('ADDRESS_4', models.CharField(max_length=30)),
 ('ADDRESS_5', models.CharField(max_length=30)),
 ('CODE',models.CharField(max_length=100))
 ('WHY', models.TextField(max_length=1000))
 ('MAILING_LIST', models.ForeignKey(User, on_delete=models.CASCADE))
            ],
        ),
        ]
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    first_name = models.CharField(max_length=30)
    surnname = models.CharField(max_length=30)
    Email = models.CharField(max_length=100)
    ADDRESS_1 = models.CharField(max_length=30)
    ADDRESS_2 = models.CharField(max_length=30)
    ADDRESS_3 = models.CharField(max_length=30)
    ADDRESS_4 = models.CharField(max_length=30)
    ADDRESS_5 = models.CharField(max_length=30)
    CODE = models.CharField(max_length=100)
    WHY= models.TextField()
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    MAILING_LIST = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
   
    content = models.TextField()
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
   return self.title + '  |' + str(self.title_tag)  + '  |' + str(self.author) + '  |' + str(self.body)+ '  |' +(self.first_name) + '  |' + str(self.surnname) + '  |' + str(self.Email)+ '  |' + str (self.ADDRESS_1)+ '  |' + str(self.ADDRESS_2)+ '  |' + str(self.ADDRESS_3)+ '  |' + str(self.ADDRESS_4)+ '  |' + str(self.ADDRESS_5)+ '  |' + str(self.CODE) + '  |' + str(self.WHY) + '  |' + '  |' + str(self.MAILING_LIST) +'  |' +'  |' + str(self.content) +'  |' + str(self.date_posted)

#def get_absolute_url(self): 
 #       return reverse('post-detail', kwargs={'pk': self.pk}) 


<br>
<input id="email" type="file" placeholder="browse">
<br>


def get_absolute_url(self): 
        #return reverse('article-detail', args=(str(self.id)))
    return reverse('home')