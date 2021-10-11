from django.db import models

# Create your models here.


class React(models.Model):
    RegnNo = models.PositiveIntegerField(
        blank=False, null=False)  # 0 to 2147483647

    ApplicantName = models.CharField(max_length=30, blank=False, null=False)

    select = [
        ("KA", "KA"),
        ("TN", "TN"),
        ("JK", "JK"),
        ("AP", "AP"),
        ("TS", "TS"),
        ("AN", "AN"),
        ("NL", "NL"),
    ]
    State = models.CharField(
        max_length=2,
        choices=select,
        default="KA",
    )
