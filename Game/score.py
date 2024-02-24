from .models import PlayerRecord
from .settings import MAX_RECORDS_NUMBER, SCORE_FILE

class GameRecord:
    def __init__(self) -> None:
        self.records = []

    def add_record(self, record: PlayerRecord) -> None:
        existing_record = next((r for r in self.records if r == record), None)
        if existing_record:
            if record > existing_record:
                self.records.remove(existing_record)
                self.records.append(record)
        else:
            self.records.append(record)

    def prepare_records(self) -> None:
        self.records.sort(reverse=True)
        self.records = self.records[:MAX_RECORDS_NUMBER]

class ScoreHandler:
    def __init__(self) -> None:
        self.game_record = GameRecord()
        self.file_name = SCORE_FILE

    def read(self) -> None:
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    data = line.strip().split('|')
                    name = data[0].strip()
                    mode = data[1].strip()
                    score_str = data[2].strip()

                    try:
                        score = int(score_str)
                    except ValueError:
                        continue

                    record = PlayerRecord(name, mode, score)
                    self.game_record.add_record(record)
        except FileNotFoundError:
            pass

    def save(self) -> None:
        with open(self.file_name, 'w') as file:
            for record in self.game_record.records:
                file.write(f"{record}\n")

    def display(self) -> None:
        print("| Имя | Режим   | Очки |")
        print("|------|--------|-------|")
        for record in self.game_record.records:
            print(f"{record} |")

    def add_score(self, player_name: str, mode: str, score: int) -> None:
        record = PlayerRecord(player_name, mode, score)
        self.game_record.add_record(record)
