from rest_framework import serializers
#from protocolApplication.models import Film
from protocolApplication.models import TaskDetails

class TaskSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)

    class Meta:
        model = TaskDetails
        fields = ('id', 'name', 'date', 'startTime', 'amountOfTime', 'descriptionOfTheTask', 'image')