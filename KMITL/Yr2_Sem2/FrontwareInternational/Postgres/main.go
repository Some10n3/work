package main

import (
	"database/sql"
	"fmt"
	"html/template"
	"log"
	"net/http"

	_ "github.com/lib/pq"
	// "go.mongodb.org/mongo-driver/mongo/description"
)

const (
	dbHost     = "localhost"
	dbPort     = 5432
	dbName     = "postgres"
	dbUser     = "postgres"
	dbPassword = "123456"
)

var db *sql.DB

type Item struct {
	ID    int
	Name  string
	Price float64  // Change the type to float64
	Picture string
	Description string
}

func main() {
	// Connect to PostgreSQL database
	dbInfo := fmt.Sprintf("host=%s port=%d dbname=%s user=%s password=%s sslmode=disable", dbHost, dbPort, dbName, dbUser, dbPassword)
	var err error
	db, err = sql.Open("postgres", dbInfo)
	if err != nil {
		log.Fatal("Error connecting to database:", err)
	}
	defer db.Close()

	// Serve HTML file and handle form submission
	http.HandleFunc("/", listHandler)
	http.HandleFunc("/insert", insertHandler)

	// Start the server
	log.Println("Server started on http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func listHandler(w http.ResponseWriter, r *http.Request) {
	// Query the database to retrieve the list of items
	rows, err := db.Query("SELECT id, name, price, picture, description FROM items")
	if err != nil {
		http.Error(w, "Error querying database", http.StatusInternalServerError)
		log.Println("Error querying database:", err)
		return
	}
	defer rows.Close()

	// Iterate through the rows and create a slice of Item structs
	var items []Item
	for rows.Next() {
		var item Item
		if err := rows.Scan(&item.ID, &item.Name, &item.Price, &item.Picture, &item.Description); err != nil {
			http.Error(w, "Error scanning row", http.StatusInternalServerError)
			log.Println("Error scanning row:", err)
			return
		}
		items = append(items, item)
	}
	if err := rows.Err(); err != nil {
		http.Error(w, "Error iterating through rows", http.StatusInternalServerError)
		log.Println("Error iterating through rows:", err)
		return
	}

	// Render HTML template with item list
	tmpl, err := template.ParseFiles("list.html")
	if err != nil {
		http.Error(w, "Error parsing template", http.StatusInternalServerError)
		log.Println("Error parsing template:", err)
		return
	}
	if err := tmpl.Execute(w, items); err != nil {
		http.Error(w, "Error executing template", http.StatusInternalServerError)
		log.Println("Error executing template:", err)
		return
	}
}

func insertHandler(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "insert.html")

	// Parse form data
	err := r.ParseForm()
	if err != nil {
		http.Error(w, "Error parsing form", http.StatusBadRequest)
		return
	}

	// Extract form values
	name := r.Form.Get("name")
	price := r.Form.Get("price")
	picture := r.Form.Get("picture")
	description := r.Form.Get("description")

	// Check latest id
	var id int
	err = db.QueryRow("SELECT id FROM items ORDER BY id DESC LIMIT 1").Scan(&id)
	if err != nil {
		if err == sql.ErrNoRows {
			// Handle case where there are no rows in the table
			id = 1 // Set id to 1 if there are no existing rows
		} else {
			// Handle other database errors
			http.Error(w, "Error querying database", http.StatusInternalServerError)
			log.Println("Error querying database:", err)
			return
		}
	} else {
		// Increment id by 1 to get the next available id
		id++
	}

	fmt.Println("id:", id)
	fmt.Println("name:", name)
	fmt.Println("price:", price)
	fmt.Println("picture:", picture)
	fmt.Println("description:", description)

	// Insert data into database
	_, err = db.Exec("INSERT INTO items(id, name, price, picture, description) VALUES($1, $2, $3, $4, $5)", id, name, price, picture, description)
	if err != nil {
		http.Error(w, "Error inserting data into database", http.StatusInternalServerError)
		log.Println("Error inserting data into database:", err)
		return
	}

	// Show success message
	fmt.Fprintf(w, "Item inserted successfully!")
}
