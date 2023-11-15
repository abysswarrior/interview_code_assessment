from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserAddScoreSerializers, ArticleListSerializers
from .models import Article, Score


class UserAddScoreView(APIView):
    serializer_class = UserAddScoreSerializers

    def post(self, request, article_id):
        article = Article.objects.get(pk=article_id)
        user = request.user

        try:
            score = Score.objects.get(article=article, user=user)
            serializer = self.serializer_class(score, data=request.data, partial=True)
        except Score.DoesNotExist:
            serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(article=article, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleListView(APIView):
    serializer_class = ArticleListSerializers

    def get(self, request):
        serializer_context = {'request': request}
        all_articles = Article.objects.all()
        ser_data = self.serializer_class(instance=all_articles, many=True, context=serializer_context).data
        return Response(ser_data, status=status.HTTP_200_OK)
