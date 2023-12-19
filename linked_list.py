from abc import ABC, abstractmethod


class InterfaceList(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def list_empty(self):
        pass

    @abstractmethod
    def list_full(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def retrieve_element(self):
        pass

    @abstractmethod
    def replace_element(self):
        pass

    @abstractmethod
    def traverse_list(self):
        pass

    @abstractmethod
    def Clear(self):
        pass


class NodeList:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.back = None


class LinkedList(InterfaceList):
    def __init__(self) -> None:
        self.head = None
        self.current = None
        self.tail = None
        self.current_index = 0
        self.size = 0

    def __str__(self):
        if self.head is None:
            return "Empty Linked List"
        else:
            current = self.head
            elements = []

            while current or len(elements) == self.size:
                elements.append(str(current.data))
                current = current.next

            return " -> ".join(elements)

    @property
    def list_empty(self):
        return self.head is None

    @property
    def list_full(self):
        return False

    def insert(self, index, element):
        """
        This feature adds a new item to the list using the place number chosen by the user.

        Parametars:
        - index (int): The number of the place where the new item will be added.
        - element (any): The value of the item to be added to the list

        Returns:
        - None
        """

        # Check if the index is out of bounds
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        new_node = NodeList(element)
        # If the location of the item where the new item will be placed is zero!
        if index == 0:
            # If the user is going to place the first item in the list, we will need to adjust some things such as the location of the back, next, and the tail.
            if self.size == 0:
                # Link the item
                new_node.next = self.head
                self.head = new_node
                self.tail = new_node
                new_node.back = self.tail
                new_node.next = self.tail

            # If the user is going to place the second item in the list in the zero position, we will need to adjust some things such as the location of the back, next, and the tail.
            elif self.size == 1:
                # Link the item
                new_node.next.back = new_node
                self.tail = new_node.next
                new_node.back = self.tail
                self.tail.next = new_node

            # If the user were to place any number of items in the zero position in the list, we would set next, back, and tail as we did before.
            elif self.size > 1:
                # Link the item
                new_node.next.back = new_node
                self.tail.next = new_node
                new_node.back = self.tail

            # In order to track the last addition made by the user
            self.current_index = 0
            self.current = self.head
            # ----------------------------------------------------

        else:
            # If the current index is farther from the location of the element that the user will place, we will return the current index so that we can link the current element between the two elements.
            if index <= self.current_index:
                while self.current_index > index:
                    self.current = self.current.back
                    self.current_index -= 1

                # Link the item
                new_node.next = self.current.next
                self.current.next = new_node
                new_node.back = self.current
                new_node.next.back = new_node

            # Here if the current index is smaller than the location of the element selected by the user
            else:
                while self.current_index != index - 1:
                    self.current = self.current.next
                    self.current_index += 1

                # Here we determine if the location of the item is equal to the number of items in the list.
                # This means that the location of the item will be the last location in the list,
                # and on it we will place the item’s linking code,
                # where the next of the item will be equal to the first item in the list and the back of the first item will be equal to the item added by the user.
                if index == self.size:
                    # Link the item
                    new_node.next = self.current.next
                    self.current.next = new_node
                    new_node.back = self.current
                    self.head.back = new_node
                    self.tail = new_node
                else:
                    # Here if the item is not the last item in the list
                    # Link the item
                    new_node.next = self.current.next
                    self.current.next = new_node
                    new_node.back = self.current
                    new_node.next.back = new_node

        # Here we supply a list counter
        self.size += 1

    def delete(self, index) -> None:
        """
        This feature deletes a specific item from the list by specifying the item index by the user.

        Parametars:
        - index (int): Item index in the list

        Returns:
        - None
        """
        if self.head is None:
            return "The list is empty"
        else:
            if index == 0:
                requerd = self.head
                self.head = requerd.next
                del requerd

                # In order to track the last addition made by the user
                self.current = self.head
                self.current_index = 0
                # ----------------------------------------------------

            else:
                if index <= self.current_index:
                    # In order to track the last addition made by the user
                    self.current = self.head
                    self.current_index = 0
                    # ----------------------------------------------------

                while self.current < index - 1:
                    self.current = self.current.next
                    self.current_index += 1

                requerd = self.current.next
                self.current.next = requerd.next  # python is son of bitch
                del requerd
            self.size -= 1

    def retrieve_element(self, index):
        if self.head is None:
            return "The list is empty"
        else:
            if index == 0:
                requerd = self.head.data
                return str(requerd)
            else:
                current = self.head
                iteretor = 0

                while iteretor < index - 1:
                    current = current.next
                    iteretor += 1

                requerd = current.next
                return str(requerd.data)  # python is son of bitch

    def replace_element(self, index_old_element, new_element):
        if self.head is None:
            return "The list is empty, you must be insert element by feature insert()"
        else:
            current = self.head
            iteretor = 0

            while iteretor < index_old_element:
                if current is None:
                    return "Index out of range"
                else:
                    current = current.next
                    iteretor += 1
            current.data = new_element
            return (
                f"The element '{new_element}' become in index {index_old_element} now."
            )

    def traverse_list(self):
        if self.list_empty:
            return "The list is empty"
        else:
            current = self.head
            iteretor = 0
            while current is not None:
                element = current
                current = current.next
                iteretor += 1
                print(str(element.data))
                if element.next is None:
                    break

    def Clear(self):
        if self.list_empty:
            return "The list is empty"
        else:
            current = self.head
            iteretor = 0

            while current is not None:
                node = current.next
                del current
                iteretor += 1
                current = node

            self.head = None
            self.size = 0
            return "All items have been deleted"


class ArrayList(InterfaceList):
    def __init__(self, max_size) -> None:
        self.data = []
        self.size = 0
        self.max_size = max_size

    def __str__(self) -> str:
        return str(self.data)

    @property
    def list_empty(self):
        return self.size == 0

    @property
    def list_full(self):
        return self.size == self.max_size

    def insert(self, index, element):
        if not self.list_full:
            self.data.insert(index, element)
            self.size += 1
        else:
            raise Exception("The list is full, the operation failed")

    def delete(self, index):
        if not self.list_empty:
            data = self.data.pop(index)
            self.size -= 1
            return data
        else:
            raise Exception("The list is empty, the operation failed")

    def retrieve_element(self, index):
        data = self.data
        return data[index]

    def replace_element(self, index_old_element, new_element):
        data = self.data
        data[index_old_element] = new_element
        return f"The element '{new_element}' become in index {index_old_element} now."

    def traverse_list(self):
        if not self.list_empty:
            for element in self.data:
                print(element)

    def Clear(self):
        self.data.clear()
        self.size = 0
        return True
