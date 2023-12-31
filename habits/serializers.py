from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from habits.models import Habit
from habits.validators import HabitDuration, HabitRelatedIsPleasant, HabitRewardOrRelatedIsPleasant, \
    HabitRelatedOrIsPleasant


class HabitSerializer(serializers.ModelSerializer):

    class Meta:

        model = Habit
        fields = '__all__'

        validators = [
            HabitDuration(
                # queryset=Habit.objects.values_list('duration'),
            ),

            HabitRelatedIsPleasant(
                # queryset=Habit.objects.values_list('related_habit', 'habit__is_pleasant'),
            ),

            HabitRewardOrRelatedIsPleasant(
                # queryset=Habit.objects.values_list('related_habit', 'reward'),
            ),

            HabitRelatedOrIsPleasant(
                # queryset=Habit.objects.values_list('is_pleasant', 'related_habit', 'reward'),
            )

        ]
