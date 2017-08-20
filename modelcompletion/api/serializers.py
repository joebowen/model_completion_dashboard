from rest_framework import serializers

class StringListField(serializers.ListField):
    child = serializers.CharField()

class CellSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)

class IonChannelSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()

class NeuronSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()

class NeuronDetailSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    celltype=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()
    receptors = StringListField()
    type = StringListField()
    innexin= StringListField()
    neurotransmitter = StringListField()
    neuropeptide = StringListField()


class ChannelDetailSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=200)
    completeness = serializers.IntegerField()
    celltype=serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=10000)
    gene_name = serializers.CharField(max_length=200)
    gene_WB_ID = serializers.CharField(max_length=200)
    gene_class = serializers.CharField(max_length=200)
    expression_pattern = serializers.CharField(max_length=200)
    neuroML_file = serializers.CharField(max_length=500)

class MuscleDetailSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    celltype=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()
    neurons= StringListField()
    receptors = StringListField()



class MuscleSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()

class ChannelSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()

class BodyMuscleSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()

class PharynxMuscleSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()
