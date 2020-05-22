
"""
You have been given a robot with very basic capabilities:

It can move left or right.
It can pick up an item
If it tries to pick up an item while already holding one, it will swap the items instead.
It can compare the item it's holding to the item in front of it.
It can switch a light on its head on or off.
Your task is to program this robot to sort lists using ONLY these abilities.

R̲u̲l̲e̲s̲:̲
Inside the robot_sort directory you'll find the robot_sort.py file. Open it up and read through each of the robot's abilities. Once you've understood those, start filling out the sort() method following these rules:

Y̲o̲u̲ m̲a̲y̲ u̲s̲e̲ a̲n̲y̲ p̲r̲e̲-̲d̲e̲f̲i̲n̲e̲d̲ r̲o̲b̲o̲t̲ m̲e̲t̲h̲o̲d̲s̲.̲
Y̶o̶u̶ m̶a̶y̶ N̶O̶T̶ m̶o̶d̶i̶f̶y̶ a̶n̶y̶ p̶r̶e̶-̶d̶e̶f̶i̶n̶e̶d̶ r̶o̶b̶o̶t̶ m̶e̶t̶h̶o̶d̶s̶.̶
You may use logical operators. (if, and, or, not, etc.)
You may use comparison operators. (>, >=, <, <=, ==, is, etc.)
You may use iterators. (while, for, break, continue)
Y̶o̶u̶ m̶a̶y̶ N̶O̶T̶ s̶t̶o̶r̶e̶ a̶n̶y̶ v̶a̶r̶i̶a̶b̶l̶e̶s̶.̶ (=)
Y̶o̶u̶ m̶a̶y̶ N̶O̶T̶ a̶c̶c̶e̶s̶s̶ a̶n̶y̶ i̶n̶s̶t̶a̶n̶c̶e̶ v̶a̶r̶i̶a̶b̶l̶e̶s̶ d̶i̶r̶e̶c̶t̶l̶y̶.̶ (̶s̶e̶l̶f̶.̶_̶a̶n̶y̶t̶h̶i̶n̶g̶)̶
Y̶o̶u̶ m̶a̶y̶ N̶O̶T̶ u̶s̶e̶ a̶n̶y̶ P̶y̶t̶h̶o̶n̶ l̶i̶b̶r̶a̶r̶i̶e̶s̶ o̶r̶ c̶l̶a̶s̶s̶ m̶e̶t̶h̶o̶d̶s̶.̶ (̶s̶o̶r̶t̶e̶d̶(̶)̶,̶ e̶t̶c̶.̶)̶
You may define robot helper methods, as long as they follow all the rules.

"""
"""
Hints
Make sure you understand the problem and all of the rules!
A solution that breaks the rules will not receive full credit.

If you're unsure if an operator or method is allowed, ask.

Lay out some numbered cards in a line and try sorting them as if you were the robot.

Come up with a plan and write out your algorithm before coding. If your plan is sound but you don't reach a working implementation in three hours, you may receive partial credit.

There is no efficiency requirement but you may lose points for an unreasonably slow solution. Tests should run in far less than 1 second.

We discussed a sorting method this week that might be useful. Which one?

The robot has exactly one bit of memory: its light. Why is this important?

"""


class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        """
        1. First and formost w̲e̲ n̲e̲e̲d̲ t̲o̲ s̲o̲r̲t̲
         the robot's list.
                - W̶e̶ c̶a̶n̶n̶o̶t̶ u̶s̶e̶ (̶s̶o̶r̶t̶.̶(̶)̶)̶
                - Hint states laying out some number cards in a line. e.g.,  ♠ ♡ ♢ ♣ ♤ deck of cards  B̲u̲b̲b̲l̲e̲ S̲o̲r̲t̲ A̲l̲g̲o̲r̲i̲t̲h̲m̲.
                - Selection Sort has a runtime of O(n²)
        2. B̲u̲b̲b̲l̲e̲ S̲o̲r̲t̲ A̲l̲g̲o̲r̲i̲t̲h̲m̲:
                -  Will need to compare the first and second item of our collection.
                -   If our first item is bigger than our second item, we swap.
        3. Will move to our next item and compare the second item with the third item.
                - if our second item is bigger than our third, swap the items.
        4.  Will do this for every item until the end of the list.
        5. Repeating steps 2-4( decrementing "the end of the list" by 1 each time).
        6. self.swap_item
            - swap item with current held item with self.postion
        7. self.compare_item
            - will then compare current held with item in self.position
        8.  self. can_move_right checks if it can move right.
        9.  self. can_move_left will check if can move left
        10. check if it can move left
                - self.move_left
                - moves positon -1
        11. self.move_right
                - moves positon +1
        """
        """
        🄸🄽 🄲🄾🄽🄲🄻🅄🅂🄸🄾🄽:
        We implemented our bubble sort by placing none in our first column. Then comparing each item. We will need to move right, reach, etc. Will keep swaping items and continue repeating .
            1 - swap item
            2 - move right
            3 - compare item
                - if item is (>) greater will swap item
             - repeat 1-3
            4 - Selection Sort has a runtime of O(n²)

        """
        """
        Print statements:
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)
        """

        self.set_light_on()
        while self.light_is_on():

            self.set_light_off()
            while(self.can_move_right()):
                # pick up item one
                # print("Sorting:")
                # print(f"picked up {self._item}")
                self.swap_item()
                # move right
                # print("move right")
                self.move_right()
                # comparing:
                # [0-99]
                if(self.compare_item() == 1):
                    # - 1 reverses numbers 99-0
                    # if item two is greater swap
                    # turns the lights on
                    self.set_light_on()
                    # print("light on")
                    # print(f"swapped with {self._item}, light is {self._light}")
                    self.swap_item()

                    # we are reseting for our next iteration
                self.move_left()
                self.swap_item()
                # print(f"moved to {self._position} and swapped for {self._item}")
                self.move_right()
                if self.can_move_right() == False and self.light_is_on() == True:
                    while self.can_move_left() == True:
                        self.move_left()
                        self.set_light_off()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [5, 3, 2, 4, 1]

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
