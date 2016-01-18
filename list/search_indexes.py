from haystack import indexes
from list.models import Book
from list.search_backends import CustomEdgeNgramField

__author__ = 'justin'


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = CustomEdgeNgramField(document=True, use_template=True, index_analyzer="edgengram_analyzer",
                                search_analyzer="standard")
    # authors = indexes.MultiValueField()
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        results = self.get_model().objects.all()

        print(results)

        return results

    def prepare_authors(self, obj):
        return [i for i in obj.author.all()]
