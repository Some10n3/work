from pyswip import Prolog

def test_prolog_query():
    # Initialize Prolog engine
    prolog = Prolog()

    # Load the Prolog file
    prolog.consult('test.pl')

    # Run a simple query
    query = "man(X)"
    result = list(prolog.query(query))

    # Print the results
    print("Results from Prolog:")
    for item in result:
        print(item)

# Run the test
test_prolog_query()
