from django.db import models
from django.core.validators import MinValueValidator

class Question(models.Model):
    Monthly = 30
    Fortnightly = 14
    Weekly = 7
    freq_choices = [
        (Monthly, 'Monthly'),
        (Fortnightly, 'Fortnightly'),
        (Weekly, 'Weekly')
    ]
    total_savings = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    rent = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    electricity = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    gas = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    water = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    internet = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    mobile = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    transport = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    food = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    clothes = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    other = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )
    freq_rent = models.DecimalField(
        verbose_name="",
        max_digits=20,
        decimal_places=2,
        max_length=3,
        choices=freq_choices,
        default=Monthly,
    )
    freq_elec = models.DecimalField(
        verbose_name="",
        max_digits=20,
        decimal_places=2,
        max_length=3,
        choices=freq_choices,
        default=Monthly,
    )
    freq_gas = models.DecimalField(
        verbose_name="",
        max_digits=20,
        decimal_places=2,
        max_length=3,
        choices=freq_choices,
        default=Monthly,
    )
    freq_water = models.DecimalField(
        verbose_name="",
        max_digits=20,
        decimal_places=2,
        max_length=3,
        choices=freq_choices,
        default=Monthly,
    )
    freq_internet = models.DecimalField(
        verbose_name="",
        max_digits=20,
        decimal_places=2,
        max_length=3,
        choices=freq_choices,
        default=Monthly,
    )
    freq_mobile = models.DecimalField(
        verbose_name="",
        max_digits=20,
        decimal_places=2,
        max_length=3,
        choices=freq_choices,
        default=Monthly,
    )
    freq_transport = models.DecimalField(
        verbose_name="",
        max_digits=20,
        decimal_places=2,
        max_length=3,
        choices=freq_choices,
        default=Monthly,
    )
    freq_food = models.DecimalField(
        verbose_name="",
        max_digits=20,
        decimal_places=2,
        max_length=3,
        choices=freq_choices,
        default=Monthly,
    )
    freq_clothes = models.DecimalField(
        verbose_name="",
        max_digits=20,
        decimal_places=2,
        max_length=3,
        choices=freq_choices,
        default=Monthly,
    )
    freq_other = models.DecimalField(
        verbose_name="",
        max_digits=20,
        decimal_places=2,
        max_length=3,
        choices=freq_choices,
        default=Monthly,
    )
