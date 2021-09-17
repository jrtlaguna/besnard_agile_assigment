from django.core.management import base, call_command, CommandError


class Command(base.BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Calculating user URFs and tiers...")
        try:
            call_command("loaddata", "values")
            call_command("loaddata", "principles")

        except Exception as e:
            CommandError(e)
