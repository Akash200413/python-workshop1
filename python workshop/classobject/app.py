class Application:

    def __init__(self, application_name, category, company, app_size, no_of_users, ratings):
        self.application_name = application_name
        self.category = category
        self.company = company
        self.app_size = app_size
        self.no_of_users = no_of_users
        self.ratings = ratings

    def signup(self):
        print(f"Signup done... {self.application_name}")

    def login(self):
        print(f"Welcome to {self.application_name}")

    def logout(self):
        print("Thank you for using this app")


# Creating objects
app1 = Application(
    application_name="Instagram",
    category="Social Media",
    company="Meta",
    app_size="42.478MB",
    no_of_users="12225",
    ratings="10"
)

app2 = Application(
    application_name="Facebook",
    category="Social Media",
    company="Meta",
    app_size="90MB",
    no_of_users="123",
    ratings="4.5"
)

app3 = Application(
    application_name="YouTube",
    category="Video Platform",
    company="Google",
    app_size="42.478MB",
    no_of_users="12225",
    ratings="10"
)
