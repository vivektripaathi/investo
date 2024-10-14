from django.urls import path
from .views import sma_crossover_strategy

urlpatterns = [
    path('sma-crossover/', sma_crossover_strategy, name='sma_crossover_strategy'),
]
