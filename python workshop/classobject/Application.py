class Application:

    def __init__(self,application_name,catogary,company,app_size,no_of_users,ratings):
        self.application_name=application_name
        self.catogary=catogary
        self.company=company
        self.app_size=app_size
        self.no_of_user=no_of_users
        self.ratings=ratings

    def singup(self):
        print(f"signup done,{self.application_name}")
    def login(self):
        print(f"welcome to {self.application_name}")
    def logout(self):
        print("thankyou for using this app")

    def info(self):
        print(self.application_name, "\n", self.catogary, "\n", self.company, "\n", self.app_size, "\n", self.ratings)

app1=Application("instagram","social media","meta",42.478,12225,9.8)
app2=Application("facbook","social media","meta",90,17000,4.5)
app3=Application("youtube","social media","meta",42.478,18977,8.0)
app1.singup()
app1.login()
app1.logout()
app1.info()

app2.singup()
app2.login()
app2.logout()
app2.info()

app3.singup()
app3.login()
app3.logout()
app3.info()