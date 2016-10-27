from django.shortcuts import render
# from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from menu_api.models import Special, Ingredient
from menu_api.serializers import SpecialSerializer, IngredientSerializer
from menu_api.permissions import IsCreatedByOrReadOnly


# class SpecialListAPIView(ListAPIView):
#     queryset = Special.objects.all()
#     serializer_class = SpecialSerializer

class SpecialListCreateAPIView(ListCreateAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer

    def perform_create(self, serializer):
        # print(args) # in case you don't know what method sig is or looks like
        # print(kwargs)
        print(serializer)
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)  # dmz


class SpecialDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer
    permission_classes = (IsCreatedByOrReadOnly, )


class IngredientListCreateAPIView(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetailAPIView(RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
