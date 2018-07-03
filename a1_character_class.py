"""
Create the Character class for Mage or Rouge.
"""
from typing import Any
# from a1_battle_queue import BattleQueue
# from a1_playstyle import RandomPlaystyle, ManualPlaystyle


class Character:
    """
    Character class for the character, either Rouge or Mage
    """
    health_points: int
    skill_points: int
    enemy: "Character"

    def __init__(self, char_name: str, battle_queue: "BattleQueue",
                 playstyle: "Playstyle") -> None:
        """
        Initialize a character with name char_name character type char_type,
        either Rouge or Mage
        """
        self.char_name = char_name.strip()
        self.animation_state = []
        self.health_points = 100
        self.skill_points = 100
        self.battle_queue = battle_queue
        # self.character = self.battle_queue.peek()
        self.playstyle = playstyle
        self.enemy = None
        # self.defence = 0

    def __repr__(self) -> str:
        """
        Create a representation of the character in the format:
        Sophia (Rogue): 100/100 for a Rogue named Sophia

        >>> from a1_battle_queue import BattleQueue
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue("Sophia", bq, ps)
        >>> c
        Sophia (Rogue): 100/100
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Return a str representation of the character.
        """

        raise NotImplementedError

    def get_name(self) -> str:
        """
        Return the name of the character.
        >>> from a1_battle_queue import BattleQueue
        >>> from a1_playstyle import RandomPlaystyle
        >>> bq = BattleQueue
        >>> ps = RandomPlaystyle(bq)
        >>> r = Rogue("Sophia", bq, ps)
        >>> m = Mage("Ashas", bq, ps)
        >>> r.get_name()
        'Sophia'
        >>> m.get_name()
        'Ashas'
        """
        return self.char_name

    def get_hp(self) -> float:
        """
        return the health points for character.

        >>> from a1_battle_queue import BattleQueue
        >>> from a1_playstyle import RandomPlaystyle
        >>> bq = BattleQueue
        >>> ps = RandomPlaystyle(bq)
        >>> r = Rogue("Sophia", bq, ps)
        >>> m = Mage("Ashas", bq, ps)
        >>> r.get_hp()
        100
        """

        return self.health_points

    def get_sp(self) -> float:
        """
        Return the skill points for character.
        >>> from a1_battle_queue import BattleQueue
        >>> from a1_playstyle import RandomPlaystyle
        >>> bq = BattleQueue
        >>> ps = RandomPlaystyle(bq)
        >>> r = Rogue("Sophia", bq, ps)
        >>> m = Mage("Ashas", bq, ps)
        >>> r.get_sp()
        100
        """

        return self.skill_points

    def is_valid_action(self, action: Any) -> bool:
        """
        Return whether the action action is a valid action to perform.
        Action should be either "A" or "S", anything else returns False.
        """

        raise NotImplementedError

        # if action in ["A", "S"]:
        #     if action == "A":

        # finish the implimentation of this function

    def get_next_sprite(self) -> Any:
        """
        return the next sprite
        """
        raise NotImplementedError

    def get_available_actions(self) -> list:
        """
        Get the actions that the current player can make. should be a list
        containing "A" and or "S" or an empty list if there are no actions.
        """
        raise NotImplementedError

        # return "{} ({}): {}/{}".format(self.char_name, self.char_type,
        #                                self.health_points, self.skill_points)

    def attack(self) -> None:
        """
        Perform a normal attack unique to the character.

        """
        raise NotImplementedError

    def special_attack(self) -> None:
        """
        Perform the special attack unique for each character.
        """
        raise NotImplementedError


class Rogue(Character):
    """
    Create the Rougue character. Inheriting from Character class
    """

    def __init__(self, char_name: str, battle_queue: "BattleQueue",
                 playstyle: "Playstyle") -> None:
        """
        Initialize a Rogue with name char_name, a battle queue battle_queue
        and playstyle playstyle.
        """
        super().__init__(char_name, battle_queue, playstyle)
        # self.char_type = "Rogue"
        self.defence = 10
        self.animation_state = ["rogue_idle_", 0]

    def __repr__(self) -> str:
        """
        Create a representation of the character in the format:
        Sophia (Rogue): 100/100 for a Rogue named Sophia
        >>> from a1_battle_queue import BattleQueue
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue("Sophia", bq, ps)
        >>> c
        Sophia (Rogue): 100/100
        """
        # return 'Rogue'
        return "{} (Rogue): {}/{}".format(self.char_name, self.health_points,
                                          self.skill_points)

    def __str__(self) -> str:
        """
        Return a str representation of the character.
        """
        return "rogue"
        # return "{} (Rogue): {}/{}".format(self.char_name, self.health_points,
        #                                   self.skill_points)

    def is_valid_action(self, action: str) -> bool:
        """
        Return whether the action action is a valid action to perform.
        Action should be either "A" or "S", anything else returns False.

        Valid actions for a Rogue:
        "A":
            -> deals 15 damage
            -> adds Rogue to the end of the BQ
            -> takes 3 skill points
        "S":
            -> deals 20 damage
            -> adds Rogue to the end of the BQ twice
            -> takes 10 skill points
        """

        if action == "A":
            return self.skill_points >= 3
        elif action == "S":
            return self.skill_points >= 10
        return False

    def get_next_sprite(self) -> str:
        """
        return the next sprite
        """

        if self.animation_state[1] > 9:
            self.animation_state = ["rogue_idle_", 0]

        image_num = self.animation_state[1]  # 0
        string = self.animation_state[0]  # "rogue_idle_"
        # return_str = ""

        # while image_num <= 9:
        string += str(image_num)

        self.animation_state[1] += 1

        # old_state = self.animation_state[0]

        return string

    def get_available_actions(self) -> list:
        """
        Get the actions that the current player can make. should be a list
        containing "A" and or "S" or an empty list if there are no actions.
        """
        action_list = []

        if self.skill_points >= 10:
            action_list.append("S")
        if self.skill_points >= 3:
            action_list.append("A")

        # if self.battle_queue.peek().skill_points >= 10:
        #     action_list.append("A")
        # if self.battle_queue.peek().skill_points >= 3:
        #     action_list.append("S")

        return action_list

    def attack(self) -> None:
        """
        Perform a normal attack unique to the character.

        Regular attack of Rogue:
        "A":
            -> deals 15 damage
            -> adds Rogue to the end of the BQ
            -> takes 3 skill points
        """
        self.skill_points -= 3
        self.animation_state = ["rogue_attack_", 0]
        if self.enemy.health_points - (15 - self.enemy.defence) >= 0:
            self.enemy.health_points -= (15 - self.enemy.defence)
        else:
            self.enemy.health_points = 0
        self.battle_queue.add(self)

    def special_attack(self) -> None:
        """
        Perform the special attack unique for each character.

        Special attack of Rogue:
        "S":
            -> deals 20 damage
            -> adds Rogue to the end of the BQ twice
            -> takes 10 skill points
        """
        self.skill_points -= 10
        self.animation_state = ["rogue_special_", 0]

        if self.enemy.health_points - (20 - self.enemy.defence) >= 0:
            self.enemy.health_points -= (20 - self.enemy.defence)
        else:
            self.enemy.health_points = 0

        # if self.health_points < 0:
        #     self.health_points = 0
        # if self.enemy.health_points < 0:
        #     self.enemy.health_points = 0

        self.battle_queue.add(self)
        self.battle_queue.add(self)


class Mage(Character):
    """
    Create the Mage Character. Inheriting from Character class
    """

    def __init__(self, char_name: str, battle_queue: "BattleQueue",
                 playstyle: "Playstyle") -> None:
        """
        Initialize a Rogue with name char_name, a battle queue battle_queue
        and playstyle playstyle.
        """
        super().__init__(char_name, battle_queue, playstyle)
        # self.char_type = "Mage"
        self.defence = 8
        self.animation_state = ["mage_idle_", 0]

    def __repr__(self) -> str:
        """
        Create a representation of the character in the format:
        Sophia (Rogue): 100/100 for a Rogue named Sophia
        >>> from a1_battle_queue import BattleQueue
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue("Sophia", bq, ps)
        >>> c
        Sophia (Rogue): 100/100
        """
        # return 'Mage'
        return "{} (Mage): {}/{}".format(self.char_name, self.health_points,
                                         self.skill_points)

    def __str__(self) -> str:
        """
        Return a str representation of the character.
        """
        return "mage"
        # return "{} (Mage): {}/{}".format(self.char_name, self.health_points,
        #                                  self.skill_points)

    def is_valid_action(self, action: Any) -> bool:
        """
        Return whether the action action is a valid action to perform.
        Action should be either "A" or "S", anything else returns False.

        Valid actions for Mage:
        "A":
            -> deals 20 damage
            -> adds Mage to the end of the battle queue
            -> takes 5 skill points
        "S":
            -> Deals 40 damage
            -> adds its enemy to the battle queue, then ads itself
            -> takes 30 skill points
        """

        if action == "A":
            return self.skill_points >= 5
        elif action == "S":
            return self.skill_points >= 30
        return False

    def get_next_sprite(self) -> str:
        """
        return the next sprite
        """

        if self.animation_state[1] > 9:
            self.animation_state = ["mage_idle_", 0]

        image_num = self.animation_state[1]  # 0
        string = self.animation_state[0]  # "rogue_idle_"

        # return_str = ""

        # while image_num <= 9:
        string += str(image_num)
        self.animation_state[1] += 1

        return string

    def get_available_actions(self) -> list:
        """
        Get the actions that the current player can make. should be a list
        containing "A" and or "S" or an empty list if there are no actions.

        Valid actions for Mage:
        "A":
            -> deals 20 damage
            -> adds Mage to the end of the battle queue
            -> takes 5 skill points
        "S":
            -> Deals 40 damage
            -> adds its enemy to the battle queue, then ads itself
            -> takes 30 skill points
        """
        action_list = []

        if self.skill_points >= 30:
            action_list.append("S")
        if self.skill_points >= 5:
            action_list.append("A")

        return action_list

    def attack(self) -> None:
        """
        Perform a normal attack unique to the character.

        when Mage performs a NOMAL Attack:

        "A":
            -> deals 20 damage
            -> adds Mage to the end of the battle queue
            -> takes 5 skill points
        """
        self.skill_points -= 5
        self.animation_state = ["mage_attack_", 0]

        if self.enemy.health_points - (20 - self.enemy.defence) >= 0:
            self.enemy.health_points -= (20 - self.enemy.defence)
        else:
            self.enemy.health_points = 0

        self.battle_queue.add(self)

    def special_attack(self) -> None:
        """
        Perform the special attack unique for each character.

        When Mage performs a sepcial attack:
        "S":
            -> Deals 40 damage
            -> adds its enemy to the battle queue, then ads itself
            -> takes 30 skill points

        """

        self.skill_points -= 30
        self.animation_state = ["mage_special_", 0]

        if self.enemy.health_points - (40 - self.enemy.defence) >= 0:
            self.enemy.health_points -= (40 - self.enemy.defence)
        else:
            self.enemy.health_points = 0
        self.battle_queue.add(self.enemy)
        self.battle_queue.add(self)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
    import doctest
    doctest.testmod()
