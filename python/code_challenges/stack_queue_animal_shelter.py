from data_structures.queue import Queue


class AnimalShelter:
    """
    Enqueues and dequeues dogs and cats only
    """

    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        """
        Argument:
            an animal: as an obj
        Return:
            nothing -->
        This method enqueues the animals into the appropriate Queue.
        """
        if isinstance(animal, Dog):
            self.dogs.enqueue(animal)
        elif isinstance(animal, Cat):
            self.cats.enqueue(animal)
        else:
            return "Must be a Dog or a Cat"

    def dequeue(self, pref):
        """
        Argument:
            pref: as a string
        Return:
             obj: either a dog or a cat, based on preference
        This method takes in a preference and returns the correct animal.
        """
        if pref.lower() == "dog":
            return self.dogs.dequeue()
        elif pref.lower() == "cat":
            return self.cats.dequeue()
        else:
            return None


class Dog:
    pass


class Cat:
    pass
