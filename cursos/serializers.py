from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')

class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #HiperLinkes Related Field
    '''
    avaliacoes = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail'
    )
    '''
    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    media_avaliacoes = serializers.SerializerMethodField()


    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )
    def get_media_avaliacoes(self, obj):
        # tem que ter get_ e o nome da variável
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        print(media)
        if media is None:
            return 0
        return round(media * 2) / 2