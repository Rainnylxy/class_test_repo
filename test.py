class exploreThenCrypt():

    def __init__(self):
        self.key = Fernet.generate_key()
        self.name_key = os.environ["USERNAME"]
        
exploreThenCrypt()

