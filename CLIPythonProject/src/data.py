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
Network: {self.network}
Freeze: {self.freeze}
Overheating: {self.heating}
Bluescreen: {self.bluescreen}
Os Slow: {self.osslow}

---
"""
