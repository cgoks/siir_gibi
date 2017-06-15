from django.db import models

from django.core.urlresolvers import reverse
from slugify import slugify
from siirler.models import Siir

class Muzik(models.Model):
    in_adi = models.CharField(max_length = 31)
    in_bestecisi = models.CharField(max_length = 31, blank=True)
    in_icracisi = models.CharField(max_length = 31, blank=True)
    in_linki = models.URLField(max_length=255, blank=True)
    in_yeri = models.URLField(max_length=255, blank=True)
    slug = models.SlugField(
        max_length= 63,
        help_text = "A label for URL config.",
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'Müzik'
        verbose_name_plural = 'MÜZİKLER'

        ordering = ["in_adi"]

    def __str__(self):
        return self.in_adi.title()

    def save(self, *args, **kwargs):
        self.slug=slugify(self.in_adi+"-"+self.in_icracisi)
        super(Muzik, self).save(*args, **kwargs)


    # def get_absolute_url(self):
    #     return reverse('organizer_tag_detail', kwargs={'slug': self.slug})


class Okuma(models.Model):
    in_siiri = models.ForeignKey(Siir, related_name="okumalari")
    in_muziki = models.ForeignKey(Muzik, blank=True, related_name="kullanimlari")
    in_muzik_basi = models.DecimalField("muzikin_basi", default=0, max_digits=5, decimal_places=2, blank=True)
    in_muzik_sonu = models.DecimalField("muzikin_sonu", default=0, max_digits=5, decimal_places=2, blank=True)
    in_toplam_saniyesi = models.DecimalField("toplam(sn)", default=0, max_digits=5, decimal_places=2, blank=True)
    in_tarihi = models.DateField("okuma_tarihi", blank=True, null=True)
    in_yeri = models.URLField(max_length=255, blank=True)
    slug = models.SlugField(
        max_length= 63,
        help_text = "A label for URL config.",
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'Okuma'
        verbose_name_plural = 'OKUMALAR'
        ordering = ["in_siiri"]
        get_latest_by = "in_tarihi"

    def __str__(self):
        return (self.in_siiri.in_adi.title() + " with " + self.in_muziki.in_adi.title())

    def save(self, *args, **kwargs):
        self.slug=slugify(self.in_siiri.in_adi+"-"+self.in_muziki.in_adi)
        super(Okuma, self).save(*args, **kwargs)



    # def get_absolute_url(self):
    #     return reverse('organizer_startup_detail', kwargs={'slug': self.slug})