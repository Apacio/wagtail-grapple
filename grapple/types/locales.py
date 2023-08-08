import graphene
from graphene_django import DjangoObjectType
from wagtail.models import Locale


class LocaleType(DjangoObjectType):
    language_display = graphene.String()

    class Meta:
        model = Locale

    def resolve_language_display(self, info):
        return self.get_display_name()
