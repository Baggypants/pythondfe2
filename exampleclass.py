class Dog:
    energy = "high"

    def speak(self, dognoise):
        dogsay = f"I like to say {dognoise} my energy is {self.energy}"
        return dogsay



bilbo_waggins = Dog()
havoc = Dog()
havoc.energy = "ultimate"

dogsay = bilbo_waggins.speak('meow')

havsay = havoc.speak('yipyipyip')
print(f" The waggins says {dogsay}")
print(f" The havoc says {havsay}")

#help(bilbo_waggins)