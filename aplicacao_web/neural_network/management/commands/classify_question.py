from django.core.management.base import BaseCommand
from neural_network.utils import classify_question

class Command(BaseCommand):
    help = "Recebe uma pergunta por argumento e retorna o nível de dificuldade dela"

    def add_arguments(self, parser):
        parser.add_argument("question", type=str, help="Pergunta a ser realizada")


    def handle(self, *args, **options):
        difficulty = classify_question(options['question'])

        print(f"A pergunta é categorizada como '{difficulty}'.")
