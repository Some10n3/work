from pyswip import Prolog
import turtle

def get_prolog_tree_steps(size):
    # Initialize Prolog engine
    prolog = Prolog()

    # Load the Prolog file
    prolog.consult('draw_tree.pl')

    # Run the query to get the drawing steps
    query = f"drawTree({size}, L)"
    result = list(prolog.query(query))

    if result:
        return result[0]['L']  # Return the list L from the Prolog query
    return []

def execute_steps(steps):
    for step in steps:
        command = step[0]
        value = step[1] if len(step) > 1 else None
        
        if command == 'fd':
            turtle.forward(value)
        elif command == 'backward':
            turtle.backward(value)
        elif command == 'lt':
            turtle.left(value)
        elif command == 'rt':
            turtle.right(value)

def draw_tree_from_prolog(steps):
    turtle.speed(1)
    turtle.left(90)  # Start by pointing upwards

    execute_steps(steps)

    turtle.done()

# Example usage
prolog_steps = get_prolog_tree_steps(25)
print("Drawing steps:", prolog_steps)
draw_tree_from_prolog(prolog_steps)
