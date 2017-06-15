from django.db import models

from django.core.urlresolvers import reverse
from slugify import slugify

class Sair(models.Model):

    in_adi = models.CharField(max_length=31,
        db_index=True)
    in_dogumu = models.IntegerField("sairin_dogum_senesi", blank=True, null=True)
    in_vefati = models.IntegerField("sairin_vefat_senesi", blank=True, null=True)
    websitesi = models.URLField(max_length=255, blank=True)
    slug = models.SlugField(
        max_length=63,
        help_text = "A label for URL config.",
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'ŞAİR'
        verbose_name_plural = 'ŞAİRLER'
        ordering = ["in_adi"]
 
    def __str__(self):
        return self.in_adi.title()

    def save(self, *args, **kwargs):
        self.slug=slugify(self.in_adi)
        super(Sair, self).save(*args, **kwargs)


    # def get_absolute_url(self):
    #     return reverse('organizer_startup_detail', kwargs={'slug': self.slug})


class Kitap(models.Model):
    in_adi = models.CharField(max_length=63)
    in_yazari = models.CharField(max_length=63, blank=True)
    in_basim_senesi = models.IntegerField(
        blank=True)
    slug = models.SlugField(
        max_length=36,
        help_text = "A label for URL config.",
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'Kitap'
        verbose_name_plural = 'KİTAPLAR'
        ordering = ["-in_yazari"]
        get_latest_by = "in_basim_senesi"

    def __str__(self):
        return "{} : {}".format(
            self.in_adi.title(), self.in_basim_senesi)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.in_adi+"-"+str(self.in_basim_senesi))
        super(Kitap, self).save(*args, **kwargs)


class Siir(models.Model):
    in_adi = models.CharField(max_length = 31, 
        unique=True)
    in_kaydi = models.FileField(blank=True, null=True, upload_to="kayitlar/")
    in_sairi = models.ForeignKey(Sair, blank=True, related_name="sairin_siirleri")
    in_kendi = models.TextField(blank=True)
    in_tarihi = models.IntegerField("siirin_tarihi", blank=True, null=True)
    in_kitabi = models.ForeignKey(Kitap, blank=True, null=True, related_name="kitaptaki_siirleri")
    slug = models.SlugField(
        max_length=63,
        help_text = "A label for URL config.",
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'ŞİİR'
        verbose_name_plural = 'ŞİİR'
        ordering = ["in_sairi"]

    def __str__(self):
        return self.in_adi.title() + " by " + self.in_sairi.in_adi.title()

    def save(self, *args, **kwargs):
        self.slug=slugify(self.in_adi+"-"+self.in_sairi.in_adi)
        super(Siir, self).save(*args, **kwargs)


    # def get_absolute_url(self):
    #     return reverse('organizer_tag_detail', kwargs={'slug': self.slug})


