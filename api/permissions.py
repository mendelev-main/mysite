from rest_framework import permissions


class IsAuthorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user performing the action is the post author
        is_author = obj.author_id == request.user.id

        # Check if the user is an admin
        is_admin = request.user.is_staff

        # Grant permission if the user is the post author or an admin
        return is_author or is_admin


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user performing the action is the vote author
        is_author = obj.user == request.user

        # Grant permission if the user is the vote author
        return is_author
