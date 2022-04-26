from rest_framework import serializers
from .models import Post, Ranking
from django.contrib.auth.models import User


# Show table of contents: title, number of users who rated this post, average ratings, and user rating
class PostSerializer(serializers.ModelSerializer):
    count_users_rank = serializers.SerializerMethodField()
    avr_users_rank = serializers.SerializerMethodField()
    user_rank = serializers.SerializerMethodField('_user_rank')

    def get_count_users_rank(self, obj):
        count = Ranking.objects.filter(post=obj.pk).count()
        return count

    def get_avr_users_rank(self, obj):
        ranks = Ranking.objects.filter(post=obj.pk)
        count = Ranking.objects.filter(post=obj.pk).count()
        r = 0
        for rank in ranks:
            r = rank.rank + r
        if r == 0:
            avr = 0
        else:
            avr = r / count
        return avr

    def _user_rank(self, obj):
        user_id = self.context.get("user_id")
        if user_id:
            user = User.objects.get(id=user_id)
            if Ranking.objects.filter(post=obj.pk, user=user).exists():
                rank = Ranking.objects.get(post=obj.pk, user=user)
                return rank.rank
            return False
        return False

    class Meta:
        model = Post
        fields = ['tittle', 'count_users_rank', 'avr_users_rank', 'user_rank']


# for POST ranking
class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ['rank']