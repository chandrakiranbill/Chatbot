from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = "Start a terminal chat with a ChatterBot instance."

    def add_arguments(self, parser):
        parser.add_argument("--reset", action="store_true",
                            help="Delete bot DB and retrain from corpus.")

    def handle(self, *args, **options):
        from chatterbot import ChatBot
        from chatterbot.trainers import ChatterBotCorpusTrainer
        import os

        db_uri = getattr(settings, "CHATTERBOT_DB_URI", None)
        if not db_uri:
            self.stderr.write("CHATTERBOT_DB_URI not configured in settings.")
            return

        sqlite_path = os.path.join(settings.BASE_DIR, "chatbot.sqlite3")
        if options["reset"] and os.path.exists(sqlite_path):
            os.remove(sqlite_path)
            self.stdout.write(self.style.WARNING("Reset bot database."))

        bot = ChatBot(
            "TermBot",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database_uri=db_uri,
            logic_adapters=[
                "chatterbot.logic.BestMatch",
                "chatterbot.logic.MathematicalEvaluation",
                "chatterbot.logic.TimeLogicAdapter",
            ],
            read_only=False,
        )

        needs_training = not os.path.exists(sqlite_path) or os.path.getsize(sqlite_path) < 4096
        if needs_training or options["reset"]:
            self.stdout.write(self.style.NOTICE("Training from chatterbot.corpus.english ..."))
            trainer = ChatterBotCorpusTrainer(bot)
            trainer.train("chatterbot.corpus.english")

        self.stdout.write(self.style.SUCCESS("Terminal chat started. Type ':quit' to exit.\n"))

        try:
            while True:
                user_text = input("you> ").strip()
                if user_text.lower() in {":q", ":quit", "exit"}:
                    self.stdout.write(self.style.SUCCESS("Goodbye!"))
                    break
                if not user_text:
                    continue
                response = bot.get_response(user_text)
                print(f"bot> {response}")
        except (KeyboardInterrupt, EOFError):
            self.stdout.write(self.style.SUCCESS("\nGoodbye!"))
