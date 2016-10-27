from rest_framework import serializers
from menu_api.models import Special, Ingredient


class SpecialSerializer(serializers.ModelSerializer):
    ingredients = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="ingredient_detail_api_view",  # tied to django urls name view
        read_only=True,
        )
    # created_by = serializers.ReadOnlyField()
    calorie_count = serializers.ReadOnlyField()  # don't need to give a source if the name is equal to source
    my_favorite = serializers.SerializerMethodField()  # pull source for field from Method, inject extra fields into API endpoint
    user = serializers.ReadOnlyField(source="created_by.id")

    def get_my_favorite(self, obj):
        return "Pancakes"

    class Meta:
        model = Special
        # fields = '__all__'
        exclude = ('created_by', )


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'
