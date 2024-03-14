from rest_framework.permissions import BasePermission , SAFE_METHODS


class AccessQuestionPermission(BasePermission):

    message = 'PERMISSION DENEID'
    def has_permission(self, request, view):
        return request.user.is_authenticated
    

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user == obj.user

