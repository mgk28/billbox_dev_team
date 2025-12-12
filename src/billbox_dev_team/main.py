# src/billbox_dev_team/main.py

from billbox_dev_team.crew import BillboxDevTeamCrew


def run():
    """
    Lance la BillBox Dev Team.
    Toutes les tâches définies dans tasks.yaml seront exécutées (processus séquentiel).
    """
    BillboxDevTeamCrew().crew().kickoff()


if __name__ == "__main__":
    run()
