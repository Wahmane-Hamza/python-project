class DeveloppeurExterne:
    def __init__(self, nom, matricule, email, taux_horaire):
        self.__nom = nom
        self.__matricule = matricule
        self.__email = email
        self.__taux_horaire = taux_horaire

    def get_nom(self):
        return self.__nom
    def set_nom(self, nom):
        self.__nom = nom
    nom = property(get_nom, set_nom)

    def get_matricule(self):
        return self.__matricule
    def set_matricule(self, matricule):
        self.__matricule = matricule
    matricule = property(get_matricule, set_matricule)

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email
    email = property(get_email, set_email)

    def get_taux_horaire(self):
        return self.__taux_horaire
    def set_taux_horaire(self, taux_horaire):
        self.__taux_horaire = taux_horaire
    taux_horaire = property(get_taux_horaire, set_taux_horaire)

    def Calcul_Salaire(self, houres, taux = None):
        if taux:
            return houres * taux
        return houres * self.__taux_horaire           

class DeveloppeurInterne(DeveloppeurExterne):
    def __init__(self, nom, matricule, email, experience):    
        super().__init__(nom, matricule, email, None)
        self.__experience = experience

    def get_experience(self):
        return self.__experience
    def set_experience(self, experience):
        self.__experience = experience
    experience = property(get_experience, set_experience)

    def Calcul_Salaire(self, houres):
        salaire_fix = 8000 if self.experience == "senior" else 5000
        taux_horaire = 200 if self.experience == "senior" else 150
        return salaire_fix + super().Calcul_Salaire(houres, taux_horaire)

dev0 = DeveloppeurExterne("zack", 111, "somthing", 110)
s = dev0.Calcul_Salaire(150)
print(s)
dev1 = DeveloppeurInterne("hamza", 102, "h@g", "junior")
s = dev1.Calcul_Salaire(15)
print(s)