from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound, APIException
from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except APIException as e:
            return Response(
                {"error": "Failed to create item", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            raise APIException(f"Unable to save item: {str(e)}")

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_update(serializer)
        except Exception as e:
            return Response(
                {"error": "Failed to update item", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return Response(serializer.data)

    def perform_update(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            raise APIException(f"Unable to update item: {str(e)}")

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except NotFound:
            return Response(
                {"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": "Failed to delete item", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return Response(
            {"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except Exception as e:
            raise APIException(f"Unable to delete item: {str(e)}")
