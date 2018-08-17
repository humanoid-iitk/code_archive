from chatterbot.chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Create a new instance of a ChatBot
popat = ChatBot("Terminal",
    storage_adapter="chatterbot.storage.sql_storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.mathematical_evaluation.MathematicalEvaluation",
        "chatterbot.logic.time_adapter.TimeLogicAdapter",
        "chatterbot.logic.best_match.BestMatch"
    ],
    input_adapter="chatterbot.input.terminal.TerminalAdapter",
    output_adapter="chatterbot.output.terminal.TerminalAdapter",
    database="../database.db"
)
popat.set_trainer(ListTrainer)
popat.train([
    "hi",
    "hello",
    "how are you",
    "why are you interested",
    "that is good to hear",
    "thank you",
    "you are welcome",
    "sorry",
    "its okay",
    "what is your name",
    "my name is popat",
])
print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        popat_input = popat.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

