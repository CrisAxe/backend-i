from dataclasses import dataclass

@dataclass
class Problem:
    network:bool
    freeze:bool
    heating:bool
    bluescreen:bool
    osslow:bool


    def __str__(self):
        return f"""

---
network: {self.title}
freeze: {self.freeze}
heating: {self.heating}
bluescreen: {self.bluescreen}
osslow: {self.osslow}

---
"""
