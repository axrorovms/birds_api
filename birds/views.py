from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Birds
from .serializer import BirdsCreateModelSerializer
from .serializer.birds_serializer import BirdsListModelSerializer, BirdsDetailListModelSerializer


class BirdsCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Birds.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = BirdsCreateModelSerializer


class BirdsListApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Birds.objects.all()
    serializer_class = BirdsListModelSerializer


class BirdsDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Birds.objects.all()
    serializer_class = BirdsDetailListModelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


"""
это мое первое решение но оно не сработало вернув:

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

и потом же решил использовать RetrieveUpdateDestroyAPIView вместо RetrieveAPIView
"""

# class BirdsDetailAPIView(RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Birds.objects.all()
#     serializer_class = BirdsDetailListModelSerializer
#
#     def get(self, *args, **kwargs):
#         birds_id = self.kwargs['id']
#         data = self.get_bird(birds_id)
#         return Response(data)
#
#     @staticmethod
#     def get_bird(birds_id):
#         bird_detail = Birds.objects.filter(id=birds_id).first()
#         if bird_detail:
#             return {
#                 'name': bird_detail.name,
#                 'color': bird_detail.color,
#                 'description': bird_detail.description,
#                 'image': bird_detail.image
#             }
#         else:
#             response_data = {"message": "there is no such bird"}
#
#         return response_data
