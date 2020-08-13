from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# @api_view()
# def posts_list(request):
#     queryset = Post.objects.all()
#     serializer = PostSerializer(queryset, many=True, context={'request': request})
#     return Response(data=serializer.data, status=status.HTTP_200_OK)

class PostsListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data                      # = request.POST/GET
        serializer = PostSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        # print(request.user)
        post = serializer.save()
        serializer = PostSerializer(instance=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



#TODO: Viewsets
#TODO: Pagination
#TODO: Search
#TODO: Filtration
#TODO: Permissions
#TODO: Get author from request
