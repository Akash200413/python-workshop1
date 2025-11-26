class Aadhar:
    def __init__(self,name,aadhar_number,dob,finger_print,retina):
        self.name=name
        self.aadhar_number=aadhar_number
        self.dob=dob
        self.finger_print=finger_print
        self.retina=retina

    def display_userdata(self):
        print(f"Return :{self__retina},Aadhar number)
        print(self.name)
        print(self.aadhar_number)
        print(self.dob)
        print(self._finger_print)
        print(self.__retina)

    var=Aadhar("prasad",123456789,"1-jan-2003","abcd","kikikik")
    var.display_userdata()


