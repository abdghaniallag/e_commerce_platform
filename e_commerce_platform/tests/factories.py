import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from e_commerce_platform.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: "cat_slug_%d" % n)
    slug = fake.lexify(text="cat_slug_??????")


register(CategoryFactory)
