from rest_framework import permissions

#  class name doesn't really matter, but it should be intuitive.


class IsCreatedByOrReadOnly(permissions.BasePermission):
    pass

    def has_object_permission(self, request, view, obj):
        # as long as person that created it is user, can do anything. return false would lock everything down. obj
        # allow anyone for a get request.
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # print(obj.created_by)
        return obj.created_by == request.user
