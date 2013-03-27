from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey
from django.utils.encoding import smart_text
from django_iban.fields import IbanAccountField
from django.template.defaultfilters import slugify


class Address(models.Model):
    first_name = models.CharField(max_length=48)
    family_name = models.CharField(max_length=48)
    company_name = models.CharField(blank=True, max_length=48)
    street = models.CharField(max_length=48)
    number = models.CharField(max_length=5,  blank=True, null=True)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)


class BankAccount(models.Model):
    account_number = IbanAccountField()
    bank_name = models.CharField(max_length=50)
    user_address = ForeignKey(Address)


class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return smart_text(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('projects_detail', (), {'slug' : self.slug})


class ProjectParticipation(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    pay_date = models.DateField(blank=True, null=True)
    bank_account = models.ForeignKey(BankAccount, blank=True, null=True)

    def is_paid(self):
        return self.pay_date

    def __unicode__(self):
        return u"{0}: {1}".format(self.project.name, self.user)

    class Meta:
        unique_together=("user", "project")