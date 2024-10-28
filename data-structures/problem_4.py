class Group:
    """
    A class to represent a group which can contain sub-groups and users.

    Attributes:
    -----------
    name : str
        The name of the group.
    groups : list[Group]
        A list of sub-groups within this group.
    users : list[str]
        A list of users in this group.
    """

    def __init__(self, _name: str) -> None:
        """
        Constructs all the necessary attributes for the Group object.

        Parameters:
        -----------
        _name : str
            The name of the group.
        """
        self.name: str = _name
        self.groups: list[Group] = []
        self.users: list[str] = []

    def add_group(self, group: 'Group') -> None:
        """
        Add a sub-group to this group.

        Parameters:
        -----------
        group : Group
            The sub-group to be added.
        """
        self.groups.append(group)

    def add_user(self, user: str) -> None:
        """
        Add a user to this group.

        Parameters:
        -----------
        user : str
            The user to be added.
        """
        self.users.append(user)

    def get_groups(self) -> list['Group']:
        """
        Get the list of sub-groups in this group.

        Returns:
        --------
        list[Group]
            A list of sub-groups.
        """
        return self.groups

    def get_users(self) -> list[str]:
        """
        Get the list of users in this group.

        Returns:
        --------
        list[str]
            A list of users.
        """
        return self.users

    def get_name(self) -> str:
        """
        Get the name of this group.

        Returns:
        --------
        str
            The name of the group.
        """
        return self.name


def is_user_in_group(user: str, group: Group) -> bool:
    """
    Check if a user is in the given group or any of its sub-groups.

    Parameters:
    -----------
    user : str
        The user to be checked.
    group : Group
        The group in which to search for the user.

    Returns:
    --------
    bool
        True if the user is found in the group or any sub-group, False otherwise.
    """
    if user is None:
        return False

    # Use a stack to implement an iterative depth-first search
    stack = [group]

    while stack:
        current_group = stack.pop()
        # Check if the user is directly in this group
        if user in current_group.get_users():
            return True

        # Add all subgroups to the stack for further exploration
        stack.extend(current_group.get_groups())

    return False

if __name__ == "__main__":
    # Testing the implementation

    # Creating groups and users
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user1 = "sub_child_user1"
    sub_child.add_user(sub_child_user1)
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # Test Case 1: User is in a nested subgroup
    print("Test Case 1")
    print(is_user_in_group("sub_child_user", parent))  # Expected output: True

    # Test Case 2: user is in a list of nested subgroup
    sub_child_user1 = "sub_child_user1"
    sub_child_user2 = "sub_child_user2"
    sub_child_user3 = "sub_child_user3"
    sub_child_user4 = "sub_child_user4"
    sub_child_user5 = "sub_child_user5"
    sub_child.add_user(sub_child_user1)
    sub_child.add_user(sub_child_user2)
    sub_child.add_user(sub_child_user3)
    sub_child.add_user(sub_child_user4)
    sub_child.add_user(sub_child_user5)

    print("Test Case 2")
    print(is_user_in_group("sub_child_user1", parent))  # Expected output: True
    print(is_user_in_group("sub_child_user2", parent))  # Expected output: True
    print(is_user_in_group("sub_child_user3", parent))  # Expected output: True
    print(is_user_in_group("sub_child_user4", parent))  # Expected output: True
    print(is_user_in_group("sub_child_user5", parent))  # Expected output: True

    # Test Case 3: user is not in a list of nested subgroup
    print("Test Case 3")
    print(not is_user_in_group("sub_child_user6", parent))  # Expected output: False
    
    # test case 4: user is in a list of subgroup
    child_user1 = "child_user1"
    child_user2 = "child_user2"
    child_user3 = "child_user3"
    child_user4 = "child_user4"
    child_user5 = "child_user5"
    child.add_user(child_user1)
    child.add_user(child_user2)
    child.add_user(child_user3)
    child.add_user(child_user4)
    child.add_user(child_user5)

    print("Test Case 4")
    print(is_user_in_group("child_user1", parent))  # Expected output: True
    print(is_user_in_group("child_user2", parent))  # Expected output: True
    print(not is_user_in_group("child_user3_", parent))  # Expected output: False
    print(is_user_in_group("child_user4", parent))  # Expected output: True
    print(is_user_in_group("child_user5", parent))  # Expected output: True

    # testcase5: empty user in group ?
    print("Test Case 5")
    print(not is_user_in_group("", parent))  # Expected output: False

    # testcase 6: check user in other group
    print("Test Case 6")
    parent_ = Group("parent_")
    print(not is_user_in_group("child_user1", parent_))  # Expected output: False

    # testcase 7: move group parent to other group
    other = Group("other")
    other.add_group(parent)
    print("testcase 7")
    print(is_user_in_group("sub_child_user1", other))  # Expected output: True
