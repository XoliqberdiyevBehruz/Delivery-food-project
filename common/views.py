from rest_framework import mixins, viewsets


class CreateListRetrieveViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.CreateModelMixin,
                                viewsets.GenericViewSet
                                ):
    pass