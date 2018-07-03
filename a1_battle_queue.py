"""
The BattleQueue class for A1.

A BattleQueue is a queue that lets our game know in what order various
characters are going to attack. The method headers and descriptions have all
been provided for you, but the implementation will depend on you.

You must replace the 'Any's in the type annotations as well as add in
the constructors for the docstring examples.
"""
# TODO: In the type annotations, replace Any with the appropriate types.
# To put a class name without importing it, just wrap the name in ''s.
# For example:
# add(self, character: 'Something') -> None:
#
# If there are multiple return types, import Union and use that. For example:
# Union[str, bool]
# from typing import Any

# from a1_playstyle import ManualPlaystyle, RandomPlaystyle
# from a1_character_class import Rogue, Mage
from typing import Union


class BattleQueue:
    """
    A class representing a BattleQueue.
    """

    # Dont need to document private attributes b/c the user shouldnt see these.
    # _queue_content: list

    def __init__(self) -> None:
        """
        Initialize this BattleQueue.

        >>> bq = BattleQueue()
        >>> bq.is_empty()
        True
        """
        self._queue_content = []
        # self.playstyle = Playstyle(self)

    def add(self, character: 'Character') -> None:
        """
        Add character to this BattleQueue.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character_class import Rogue
        >>> c = Rogue("sophia", bq, ps) #added
        >>> c2 = Rogue("Player 2", bq, ps)
        >>> c.enemy = c2
        >>> c2.enemy = c
        >>> bq.add(c)
        >>> bq.add(c2)
        >>> bq.is_empty()
        False
        >>> bq.is_over()
        False
        """
        self._queue_content.append(character)

    def remove(self) -> Union["Character", None]:
        """
        Remove and return the next character who can use a skill.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character_class import Rogue
        >>> c = Rogue("Sophia", bq, ps) #added
        >>> c2 = Rogue("Player 2", bq, ps)
        >>> c.enemy = c2
        >>> c2.enemy = c
        >>> bq.add(c)
        >>> bq.add(c2)
        >>> bq.remove()
        Sophia (Rogue): 100/100
        >>> bq.is_empty()
        False
        >>> bq.remove()
        Player 2 (Rogue): 100/100
        """
        temp_lst = []

        for char in self._queue_content:
            if char.get_available_actions() != []:
                temp_lst.append(char)

        if len(temp_lst) >= 1:
            self._queue_content.remove(temp_lst[0])
            return temp_lst[0]
        return None

    def is_empty(self) -> bool:
        """
        Return whether this BattleQueue is empty (i.e. has no players or
        has no players that can perform any actions).
        Even if there are characters in queue but cant perform
        any action, it should return none.

        >>> bq = BattleQueue()
        >>> bq.is_empty()
        True
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character_class import Rogue
        >>> c = Rogue("Sophia", bq, ps) #added
        >>> c2 = Rogue("Player 2", bq, ps)
        >>> c.enemy = c2
        >>> c2.enemy = c
        >>> bq.add(c)
        >>> bq.add(c2)
        >>> bq.is_empty()
        False
        """
        count = 0

        if self._queue_content == []:
            return True
        for char in self._queue_content:
            if char.get_available_actions() == []:
                count += 1
        return count == len(self._queue_content)

    def peek(self) -> Union["Character", None]:
        """
        Return the character at the front of this BattleQueue but does not
        remove them.

        Only return a character who is able to perform actions.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character_class import Rogue
        >>> c = Rogue("Sophia", bq, ps) # added
        >>> c1 = Rogue("p1", bq, ps)
        >>> c.enemy = c1
        >>> c1.enemy = c
        >>> bq.add(c)
        >>> bq.add(c1)
        >>> bq.peek()
        Sophia (Rogue): 100/100
        >>> bq.is_empty()
        False
        """
        to_return = None
        # moves = 0
        temp_lst = []

        if self._queue_content != []:
            for char in self._queue_content:
                if char.get_available_actions() != []:
                    temp_lst.append(char)

        if temp_lst != []:
            to_return = temp_lst[0]

        return to_return

    def is_over(self) -> bool:
        """
        Return whether the game being carried out in this BattleQueue is over
        or not.

        A game is considered over if:
            - Both players have no skills that they can use. # Fix
            - One player has 0 HP
            or
            - The BattleQueue is empty.

        >>> bq = BattleQueue()
        >>> bq.is_over()
        True
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character_class import Rogue
        >>> c = Rogue("Sophia", bq, ps)
        >>> c2 = Rogue("player 2", bq, ps)
        >>> c.enemy = c2
        >>> c2.enemy = c
        >>> bq.add(c)
        >>> bq.add(c2)
        >>> bq.is_over()
        False
        """
        no_hp = False

        if self.is_empty():
            # is_empty_q = True
            return True

        if (self.peek().get_hp() == 0 or
                self.peek().enemy.get_hp() == 0):
            return True

        # is the following repetetive??

        if (self.peek().get_available_actions() == [] and
                self.peek().enemy.get_available_actions() == []):
            return True

        return no_hp

    def get_winner(self) -> Union["Character", None]:
        """
        Return the winner of the game being carried out in this BattleQueue
        if the game is over. If the game is not over or if there is no winner
        (i.e. there's a tie), return None.

        >>> bq = BattleQueue()
        >>> bq.get_winner()
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character_class import Rogue
        >>> c = Rogue("Sophia", bq, ps) #added
        >>> c2 = Rogue("player 2", bq, ps)
        >>> bq.get_winner()
        >>> c.health_points = 0
        >>> c.enemy = c2
        >>> c2.enemy = c
        >>> bq.add(c)
        >>> bq.add(c2)
        >>> bq.get_winner()
        player 2 (Rogue): 100/100
        >>> c.skill_points = 2
        >>> c2.skill_points = 2
        >>> bq.get_winner()
        player 2 (Rogue): 100/2
        >>> c2.health_points = 0
        >>> bq.get_winner()
        >>> c.health_points = 2
        >>> c2.health_points = 2
        >>> bq.get_winner()
        """

        to_return = None

        if self.is_over():
            for char in self._queue_content:
                if char.get_hp() > 0 and char.enemy.get_hp() == 0:
                    to_return = char
                    return to_return
                elif char.get_hp == 0 and char.enemy.get_hp() > 0:
                    to_return = char.enemy
                    return to_return
        return to_return

        # to_return = None
        #
        # if not self.is_empty():
        #
        #     if not self.is_over():
        #         to_return = None
        #     elif self.is_over() and (self.peek().get_hp() > 0 and
        #                              self.peek().enemy.get_hp() == 0):
        #         to_return = self.peek()
        #     elif self.is_over() and (self.peek().get_hp() == 0 and
        #                              self.peek().enemy.get_hp() > 0):
        #         to_return = self.peek().enemy
        #
        # return to_return


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
    import doctest
    doctest.testmod()
