def data_func (name, surname, year_of_birth, city_of_resid, email, phone):
    print(name, surname, year_of_birth, city_of_resid, email, phone)


data_func(name="Vlad",                surname="Alucard",         year_of_birth="1431",
          city_of_resid="Sighisoara", email="night_son@blood.si", phone="21114311456")



data_func(name=(input("Enter your name ")),                   surname=(input("Enter your surname ")),
          year_of_birth=(input("Enter your year of birth ")), city_of_resid=(input("Enter your city_of_resid ")),
          email=(input("Enter your email ")),                 phone=(input("Enter your phone ")))





