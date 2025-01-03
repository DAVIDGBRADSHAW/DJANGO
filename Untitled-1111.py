class Rugby(models.Model):
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
return self.title + '  |' + str(self.title_tag)  + '  |' + str(self.author) + '  |' + str(self.body)+ '  |' +(self.first_name) + '  |' + str(self.surnname) + '  |' + str(self.Email)+ '  |' + str (self.ADDRESS_1)+ '  |' + str(self.ADDRESS_2)+ '  |' + str(self.ADDRESS_3)+ '  |' + str(self.ADDRESS_4)+ '  |' + str(self.ADDRESS_5)+ '  |' + str(self.CODE) + '  |' + str(self.WHY) + '  |' + '  |' + str(self.MAILING_LIST) +'  |' +'  |' + str(self.content) +'  |' + str(self.date_posted)
