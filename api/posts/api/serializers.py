from rest_framework import serializers

from posts.models import Post, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'author',
            'image_field',
            'tags',
            'width_field',
            'height_field',
            'image_alt',
            'reading_time',
            'short_summary',
            'content',
            'draft',
            'created_at',
            'updated_at',
        )
    
    def get_tags(self, obj, *args, **kwargs):
        obj = Post.objects.filter(slug=obj.slug)
        if obj.exists():
            qs_ = obj.first()
            qs = qs_.tags.all()
        else: 
            qs = []
        response = TagSerializer(qs, many=True).data
        return response
