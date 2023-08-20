from src.wordle import Wordle


file_path = 'src/data/words_frequency.txt'
wordle = Wordle(file_path)
wordle.run()
