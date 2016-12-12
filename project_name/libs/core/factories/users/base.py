
import factory


class BaseUserFactory(factory.django.DjangoModelFactory):

    password = 'password'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)
