from rest_framework import serializers
from .models import Score, Article


class UserAddScoreSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Score
        fields = ['user', 'score']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['score']

class ArticleListSerializers(serializers.ModelSerializer):
    score_count = serializers.SerializerMethodField()
    average_score = serializers.SerializerMethodField()
    user_score = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'score_count', 'average_score', 'user_score']

    def get_score_count(self, obj):
        return obj.score_count()

    def get_average_score(self, obj):
        return obj.average_score()

    def get_user_score(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            try:
                score = obj.scores.get(user=user)
                return ScoreSerializer(score).data
            except Score.DoesNotExist:
                return None
        return None
