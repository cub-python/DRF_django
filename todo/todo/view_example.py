from rest_framework.decorators import api_view, renderer_classes
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    get_object_or_404

# from users_app.filters import BrendFilter
from users_app.models import Brend
from users_app.serializers import BrendSerializer


# level 1 ApiView
class BrendAPINiew(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, format=None):
        brend = Brend.objects.all()
        serializer = BrendSerializer(brend, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass


#
# @api_view(['GET', 'POST'])   ##'POST'
# @renderer_classes([JSONRenderer,BrowsableAPIRenderer])
# def get(request):
#       if request.method == 'GET':
#         brend = Brend.objects.all()
#         serializer = BrendModelSerializer(brend, many=True)
#         # return Response(serializer.data)
#         return Response({'test':1})         ## Доп пример
#       elif request.method == 'POST':
#           pass

# level 2 Generic views
# class BrendCreateAPIView(CreateAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Brend.objects.all()
#    serializer_class = BrendModelSerializer
#
# class BrendListAPIView(ListAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Brend.objects.all()
#    serializer_class = BrendModelSerializer
#
# # #
# class BrendRetrieveAPIView(RetrieveAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Brend.objects.all()
#    serializer_class = BrendModelSerializer
# # #
# class BrendDestroyAPIView(DestroyAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Brend.objects.all()
#    serializer_class = BrendModelSerializer
#
# class BrendUpdateAPIView(UpdateAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Brend.objects.all()
#    serializer_class = BrendModelSerializer

# level 3 ViewSets

#
# class BrendViewSet(ViewSet):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#
#    def list(self,request):               #список
#        book = Brend.objects.all()
#        serializer_class = BrendModelSerializer(brend,many=True)
#        return Response(serializer_class.data)
#
#    def retrieve(self,request,pk=None):              # детализация
#        book = get_object_or_404(Brend, pk=pk)
#        serializer_class = BrendModelSerializer(book)
#        return Response(serializer_class.data)
# #     #
#    @action(detail=True, methods=['get'])
#    def only(self, request, pk=None):
#        brend = Brend.objects.get(id=pk)
#        return Response({'brend': brend.name,'id':brend.id})


# level 4 ModelViewSet (самый просто способ)
# class BookViewSet(ModelViewSet):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Brend.objects.all()
#    serializer_class = BrendModelSerializer

# @action(detail=True, methods=['get'])
# def only(self, request, pk=None):
#       brend = Brend.objects.get(id=pk)
#       return Response({'brend': brend.name,'id':brend.id})

# level 5 Custom ViewSet
#
# ListModelMixin,CreateAPIView, DestroyModelMixin,RetrieveAPIView,UpdateAPIView,GenericViewSet:
# class BookCustomViewSet(ListModelMixin,DestroyModelMixin,GenericViewSet,RetrieveAPIView,UpdateAPIView):
#     queryset =  Brend.objects.all()
#     serializer_class =  BrendModelSerializer
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


# filter
# class BrendQuerysetFilterViewSet(ModelViewSet):
#    serializer_class = BrendModelSerializer
#    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#    queryset = Brend.objects.all()
#
#    def get_queryset(self):
#        return Brend.objects.filter(name__contains='test')
#
# class BookListAPIView(ListAPIView):
#    serializer_class = BrendModelSerializer
#
#    def get_queryset(self):
#        name = self.kwargs['name']
#        return Brend.objects.filter(name__contains=name)

# class BrendModelViewSet(ModelViewSet):
#    queryset = Brend.objects.all()
#    serializer_class = BrendModelSerializer
#
#    def get_queryset(self):
#        name = self.request.query_params.get('name', '')
#        book = Brend.objects.all()
#        if name:
#            book = brend.filter(name__contains=name)
#        return brend


# DjangoFilter
# filters.py
# class BrendDjangoFilterViewSet(ModelViewSet):
#    queryset = Brend.objects.all()
#    serializer_class = BrendModelSerializer
#    # filterset_fields = ['id','name']
#    filterset_class = BrendFilter


# #PAGINATOR
class BrendLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


# # # #
# # # #
class BrendLimitOffsetPaginatonViewSet(ModelViewSet):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer
    pagination_class = BrendLimitOffsetPagination
    # BrendLimitOffsetPagination
