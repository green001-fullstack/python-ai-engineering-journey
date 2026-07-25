def decorator(function):

    def logger():
        print("=== Starting Task ===")

        function()

        print("=== Task Finished ===")

    return logger


@decorator
def train_model():
    print("Training AI model...")


train_model()