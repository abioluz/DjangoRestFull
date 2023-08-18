from rest_framework import permissions

class EhSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True

class TemPermissao(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method == 'DELETE':
            if 'cursos.delete_curso' in request.user.get_user_permissions():
                return True
        elif request.method == 'GET':
            if 'cursos.view_curso' in request.user.get_user_permissions():
                return True
        elif request.method == 'POST':
            if 'cursos.add_curso' in request.user.get_user_permissions():
                return True
        elif request.method == 'PUT':
            if 'cursos.change_curso' in request.user.get_user_permissions():
                return True
        return False

class TemPermissao2(permissions.DjangoObjectPermissions):
    permissions.DjangoObjectPermissions.perms_map[
        'GET'] = ['%(app_label)s.view_%(model_name)s']
