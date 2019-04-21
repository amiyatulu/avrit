from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
	""" A serializer for our user profiles objects. """
	class Meta:
		model = models.UserProfile
		fields = ('id', 'email', 'name', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		"""Create and return a new user."""
		user = models.UserProfile(
			email = validated_data['email'],
			name = validated_data['name']
			)
		user.set_password(validated_data['password'])
		user.save()

		return user
	def update(self, instance, validated_data):
		for attr, value in validated_data.items():
			if attr == 'password':
				instance.set_password(value)
			else:
				setattr(instance, attr, value)
		instance.save()
		return instance


class PostSerializer(serializers.ModelSerializer):
	"""A serializer for post."""
	class Meta:
		model = models.Post
		fields = "__all__"

class PostUploadSerializer(serializers.ModelSerializer):
	"""A serializer for post upload."""

	class Meta:
		model = models.PostUpload
		fields = "__all__"

class PostCommentSerializer(serializers.ModelSerializer):
	""" A serializer for post comment."""
	class Meta:
		model = models.PostComment
		fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
	"""A serializer for Review."""

	class Meta:
		model = models.Review
		fields = "__all__"

class ReviewUploadSerializer(serializers.ModelSerializer):
	"""A serializer for Review upload."""

	class Meta:
		model = models.ReviewUpload
		fields = "__all__"

class ReviewCommentSerializer(serializers.ModelSerializer):
	""" A serializer for Review comment."""
	class Meta:
		model = models.ReviewComment
		fields = "__all__"




	
