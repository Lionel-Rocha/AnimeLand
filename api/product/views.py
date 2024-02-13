from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer

# Permite apenas usuários administradores criarem produtos
class AdminOnlyCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated and request.user.is_staff

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    # Aplicar a permissão apenas para a ação de criação (POST)
    permission_classes_by_action = {'create': [AdminOnlyCreatePermission]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
