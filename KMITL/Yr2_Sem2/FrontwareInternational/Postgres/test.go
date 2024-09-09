package main

import (
	"fmt"
)

func main() {
	// save variable and print them
	var name string = "John"
	fmt.Println(name)

	var age int = 25
	fmt.Println(age)

	var result float64 = 3.14
	fmt.Println(result)

	// save multiple variables
	var (
		firstName string = "John"
		lastName  string = "Doe"
	)
	fmt.Println(firstName, lastName)

	// recieve inputs from user
	// var input string
	// fmt.Print("Enter your name: ")
	// fmt.Scanln(&input)
	// fmt.Println("Hello", input)

	// shorthand variable declaration
	// var name string = "John"
	// var name = "John"
	_name := "John"
	fmt.Println(_name)
	// these are the same

	// constant
	const pi = 3.14
	fmt.Println(pi)

	// loop and if statement
	for i := 0; i < 5; i++ {
		if i%2 == 0 {
			fmt.Println(i, "is even")
		} else {
			fmt.Println(i, "is odd")
		}
	}

	// array
	var fruits [3]string
	fruits[0] = "Apple"
	fruits[1] = "Banana"
	fruits[2] = "Mango"
	fmt.Println(fruits)

	// slice
	var fruitsSlice = []string{"Apple", "Banana", "Mango"}
	fmt.Println(fruitsSlice)

	// map
	var person = map[string]string{
		"name":    "John",
		"address": "New York",
	}
	fmt.Println(person);

	// function
	fmt.Println(add(1, 2))
	fmt.Println(subtract(5, 3))

	// struct
	type Person struct {
		Name string
		Age  int
	}

}

func add(a int, b int) int {
	return a + b
}

func subtract(a int, b int) int {
	return a - b
}
