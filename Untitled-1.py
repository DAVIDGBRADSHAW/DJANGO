
class Rugby(models.Model):
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
