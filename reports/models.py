from django.db import models


class AbstractItem(models.Model):
    """Abstract Item"""

    name = models.CharField(max_length=80, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class DepartmentType(AbstractItem):
    pass


class ProcessType(AbstractItem):
    pass


class Company(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Report(models.Model):

    """Report Model"""

    # 공통
    updated = models.DateTimeField("업데이트 날짜")
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, verbose_name="회사"
    )
    department = models.ForeignKey(
        DepartmentType, on_delete=models.CASCADE, null=True, verbose_name="부서명"
    )
    process = models.ForeignKey(
        ProcessType, on_delete=models.CASCADE, null=True, verbose_name="공정명"
    )

    operation = models.CharField("작업내용", max_length=70)
    effective_date = models.DateField(("실시 일자"))
    # 개선 전 위험성
    prev_image = models.FileField("개선 전 이미지", upload_to="notice", null=True, blank=True)
    prev_risk = models.TextField("개선 전 유해인자", null=True)
    prev_frequency = models.IntegerField("개선 전 빈도", blank=True, null=True)
    prev_importance = models.IntegerField("개선 전 중요도", blank=True, null=True)
    prev_dangerous = models.IntegerField("개선 전 위험성", blank=True, null=True)

    # 개선 후 위험성
    after_image = models.FileField(
        "개선 후 이미지", upload_to="notice", null=True, blank=True
    )
    after_risk = models.TextField("개선 전 유해인자", null=True)
    after_frequency = models.IntegerField("개선 후 빈도", blank=True, null=True)
    after_importance = models.IntegerField("개선 후 중요도", blank=True, null=True)
    after_dangerous = models.IntegerField("개선 후 위험성", blank=True, null=True)

    def __str__(self):
        return str(self.company)
