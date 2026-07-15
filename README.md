# 0x00. AirBnB clone - The console

## Description

This project is the first step of the AirBnB clone. It builds a command-line
interpreter that manages project objects from a terminal. The console will be
used to create, display, list, update, and delete objects while the rest of the
application is developed.

## Starting the Console

Run the console from the project root:

```bash
./console.py
```

## Commands

### create

Creates a new object instance, saves it, and prints its id.

```text
(hbnb) create BaseModel
```

### show

Prints the string representation of an object based on class name and id.

```text
(hbnb) show BaseModel 1234-1234-1234
```

### all

Prints all objects, or all objects of a specific class.

```text
(hbnb) all
(hbnb) all BaseModel
```

### destroy

Deletes an object based on class name and id.

```text
(hbnb) destroy BaseModel 1234-1234-1234
```

### update

Updates an object by class name, id, attribute name, and value.

```text
(hbnb) update BaseModel 1234-1234-1234 name "My First Model"
```

## Interactive Examples

Start the console and create an object:

```text
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```

Show an object:

```text
$ ./console.py
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {...}
```

List all objects:

```text
$ ./console.py
(hbnb) all
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {...}"]
```

Update an object:

```text
$ ./console.py
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 name "Test"
```

## Non-Interactive Example

Run a command without entering interactive mode:

```bash
echo "all" | ./console.py
```
