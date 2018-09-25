# coding=utf-8
import datetime

from django.db import models

# Create your models here.


class workRecordManager(models.Manager):
    def save_record(self, data):

        try:
            workRecord.objects.create(
                theme=data.get('theme'),
                content=data.get('content'),
                operator=data.get('username'),
            )
            result = {'result': True, 'message': u"保存成功"}
        except Exception, e:
            result = {'result': False, 'message': u"保存失败, %s"%e }
        return result


class workRecord(models.Model):

    theme = models.CharField(u"会议主题", max_length=64)
    content = models.TextField(u"会议内容", null=True, blank=True)
    record_time = models.DateTimeField(u"会议时间", default=datetime.datetime.now())
    operator = models.CharField(u"记录人", max_length=64)

    def __unicode__(self):
        return self.theme

    class Meta:
        verbose_name = u"会议记录"
        verbose_name_plural = u"会议记录"


