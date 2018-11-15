import datetime
import pickle

itemList  = []

class Item:
    def __init__(self, name, completed, dueDate):
        self.name = name
        self.completed = completed
        self.dueDate = dueDate

    def printItem(self):
        if self.completed == True:
            status = "Completed"
        else:
            status = "Not Completed"
        print self.name, self.dueDate.strftime("%x"), status

    def updateName(self, name):
        self.name = name

    def updateDueDate(self, dueDate):
        self.dueDate = dueDate

    def updateCompleted(self, completed):
        self.completed = completed

    def completeItem(self):
        self.updateCompleted(True)

    def umcompleteItem(self):
        self.updateCompleted(False)


def printMenu():
    print("1) Display ToDo List")
    print("2) Add Item")
    print("3) Mark Item Done")
    print("4) Exit")

def printList():
    for item in itemList:
        print(itemList.index(item)),
        print(": "),
        item.printItem()

def addItem():
    name = raw_input("Enter name of item: ")
    year = input("Enter due date year: ")
    month = input("Enter due date month: ")
    day = input("Enter due date day: ")
    newItem = Item(name, False, datetime.datetime(year, month, day))
    itemList.append(newItem)

def removeItem():
    toRemove = input("Which item? ")
    itemList.pop(toRemove)

def importList():
    print("Importing Tasks")

def exportList():
    print("Exporting Tasks")

def main():
    importList()
    option = 0
    while(option != 4):
        printMenu()
        option = input()
        if(option == 1):
            printList()
        elif(option == 2):
            addItem()
        elif(option == 3):
            removeItem()
    exportList()
if __name__ == "__main__":
    main();