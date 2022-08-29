from .permission import IsStaffEditorPermission
from rest_framework import permissions

class StaffEditorPermissionMixins():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]