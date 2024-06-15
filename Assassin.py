# Assassin.py
from typing import List
from Node import Node

class Assassin:
    def __init__(self, names: List[str]):
        if not names:
            raise ValueError("List of names must not be empty")

        self.kill_ring = Node(names[0])
        current = self.kill_ring
        for name in names[1:]:
            new_node = Node(name)
            current.next = new_node
            current = new_node
        current.next = self.kill_ring  # Making the kill ring circular
        self.graveyard = None

    def print_kill_ring(self):
        current = self.kill_ring
        while current:
            print(f"{current.name} is stalking {current.next.name}")
            current = current.next
            if current == self.kill_ring:
                break

    def print_graveyard(self):
        current = self.graveyard
        while current:
            print(f"{current.name} was killed by {current.killer}")
            current = current.next

    def kill_ring_contains(self, name: str) -> bool:
        current = self.kill_ring
        while current:
            if current.name.lower() == name.lower():
                return True
            current = current.next
            if current == self.kill_ring:
                break
        return False

    def graveyard_contains(self, name: str) -> bool:
        current = self.graveyard
        while current:
            if current.name.lower() == name.lower():
                return True
            current = current.next
        return False

    def game_over(self) -> bool:
        return self.kill_ring is None or self.kill_ring.next == self.kill_ring

    def winner(self) -> str:
        if not self.game_over():
            return None
        return self.kill_ring.name

    def kill(self, name: str):
        if self.game_over():
            raise RuntimeError("Game is over")
        
        previous = None
        current = self.kill_ring
        
        while current and current.name.lower() != name.lower():
            previous = current
            current = current.next
            if current == self.kill_ring:
                break
        
        if current.name.lower() != name.lower():
            raise ValueError(f"Name {name} not found in the kill ring")
        
        if previous is None:
            # Find the last person in the kill ring
            last = self.kill_ring
            while last.next != self.kill_ring:
                last = last.next
            # Update the head of the kill ring
            self.kill_ring = self.kill_ring.next
            last.next = self.kill_ring
        else:
            previous.next = current.next
        
        current.next = self.graveyard
        self.graveyard = current
        current.killer = previous.name if previous else last.name
