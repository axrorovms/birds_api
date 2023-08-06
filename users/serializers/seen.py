from rest_framework.serializers import ModelSerializer
from users.models.seen import Seen


class SeenListModelSerializer(ModelSerializer):
    class Meta:
        model = Seen
        fields = ('user', 'bird')

    def to_representation(self, instance: Seen):
        rep = super().to_representation(instance)
        rep['name'] = Seen.bird.name
        rep['color'] = Seen.bird.color
        rep['description'] = Seen.bird.description
        rep['image'] = Seen.bird.image

        return rep
