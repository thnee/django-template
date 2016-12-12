
class FakeAdminPermissionsMixin(object):
    """
    Implements necessary parts of a User to work with the django admin.
    Simply returns true on all permission and superuser questions.
    Not intended to be a fully compatible PermissionsMixin,
    that would implement all parts of the API,
    only implements just enough to make django admin happy.
    Don't use this if you actually want to use permissions.
    """

    def has_perm(self, *args, **kwargs):
        return True

    def has_module_perms(self, *args, **kwargs):
        return True

    @property
    def is_staff(self):
        return True

    @is_staff.setter
    def is_staff(self, value):
        pass

    @property
    def is_superuser(self):
        return True

    @is_superuser.setter
    def is_superuser(self, value):
        pass
