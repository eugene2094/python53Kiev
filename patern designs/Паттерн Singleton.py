class ConsoleLogManager:
    _instance = None

    def __init__(self):
        if ConsoleLogManager._instance is None:
            ConsoleLogManager._instance = self
        else:
            raise Exception("Only one instance of ConsoleLogManager!")

    @staticmethod
    def getInstance():
        if ConsoleLogManager._instance is None:
            ConsoleLogManager()
        return ConsoleLogManager._instance

    def log(self, message):
        print(f"Log entry: {message}")


log_manager = ConsoleLogManager.getInstance()
log_manager.log("Singleton pattern in action !")

log_manager_2 = ConsoleLogManager()
log_manager_2.log("test")