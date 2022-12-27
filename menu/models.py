from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """Модель навигационного меню"""

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'

    name = models.CharField('имя', max_length=64)
    slug = models.SlugField('url', max_length=64)

    def __str__(self) -> str:
        return f'{self.name}'

    @property
    def get_absolute_url(self):
        return reverse("menu", kwargs={"slug": self.slug})


class SubMenu(models.Model):
    """Модель навигационного меню"""

    class Meta:
        verbose_name = 'подпункт меню'
        verbose_name_plural = 'подпункты меню'

    name = models.CharField('имя', max_length=64)
    slug = models.SlugField('url', max_length=64)
    menu = models.ForeignKey(Menu,
                             verbose_name='меню',
                             on_delete=models.CASCADE,
                             related_name='menu')
    parent = models.ForeignKey('self',
                               verbose_name='родитель',
                               on_delete=models.CASCADE,
                               null=True, blank=True,
                               related_name='children')

    def __str__(self) -> str:
        return f'{self.name}'

    @property
    def children_count(self) -> bool:
        return self.children.count() != 0

    @property
    def get_absolute_url(self):
        return reverse("menu_item", kwargs={"slug": self.menu.slug, "menu_slug": self.slug})
