from rest_framework.serializers import ModelSerializer

from birds.models import Birds


class BirdsCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Birds
        exclude = ('id',)


class BirdsListModelSerializer(ModelSerializer):
    class Meta:
        model = Birds
        exclude = ('id', 'color', 'description',)


class BirdsDetailListModelSerializer(ModelSerializer):
    class Meta:
        model = Birds
        exclude = ('id',)
