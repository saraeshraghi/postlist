from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PostSerializer, RankingSerializer
from .models import Post, Ranking
from rest_framework import status
from django.contrib.auth.models import User


# Show table of contents: title, number of users who rated this post, average ratings, and user rating
class HomeView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        ser_data = PostSerializer(posts, many=True, context={'user_id': request.user.id})
        return Response(ser_data.data, status=status.HTTP_200_OK)


# post & delete Ranking
class RankingView(APIView):
    def post(self, request, pk):
        ser_rank = RankingSerializer(data=request.POST)
        user = User.objects.get(id=request.user.id)
        post = Post.objects.get(id=pk)
        if ser_rank.is_valid():
            Ranking.objects.update_or_create(user=user, post=post, defaults={'rank': ser_rank.validated_data['rank']})
            return Response(ser_rank.data, status=status.HTTP_200_OK)
        return Response(ser_rank.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = Ranking.objects.get(pk=pk)
        if request.user == user.user:
            Ranking.objects.get(pk=pk).delete()
            return Response({'messages': 'This rating has been deleted'})
        return Response({'messages': 'You can not delete this rating'})