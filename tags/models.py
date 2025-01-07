from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class TagItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        return TagItem.objects.select_related('tag')\
                .filter(
                content_type=content_type,
                object_id=obj_id
        )


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TagItem(models.Model):
    """What tag applied to what object"""
    objects=TagItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # type(Product,vudeo,article)
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey
