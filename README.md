# Random Quote Generator Using API

Welcome to the documentation for the Random Quote Generator using API, a simple and elegant Python application designed to fetch and display random quotes from the Quotable API. This application provides users with an enjoyable experience of discovering insightful and thought-provoking quotes with just a click of a button.

## Deployment

To deploy this project one must have tkinter and requests library installed.

If you don't have the respective libraries write the following in your terminal

#### For ttkthemes library:
```bash
  pip install ttkthemes
```
#### For request library: 
```bash
  pip install requests
```
## API Reference

#### Get Random Quote
Retrieve a random quote from the Quotable API.
```http
  GET /api/quotes/random
```

#### Get Specific Quote
Retrieve a specific quote from the Quotable API based on the quote ID.

```http
  GET /api/quotes/{quote_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `quote_id`      | `string` | **Required**. ID of the quote|


Please note that the actual implementation of the API and error messages may vary based on your specific implementation and error handling.
## Features
- Themed GUI:
Utilizes the ttk library to apply a themed style (specifically, "clam") for a more visually appealing graphical user interface (GUI).

- Dynamic Content Display:
Dynamically updates the displayed quote on the GUI with each button click without requiring manual refresh.

- Responsive Design:
Adjusts the window size to an initial size of 500x300 pixels to create a responsive design suitable for the application.

- Random Quote Generation:
Fetches a random quote from the Quotable API 
```http
(https://api.quotable.io/random)
```
 when the "Generate Quote" button is clicked.

- User Interface Elements:
Includes labels and buttons to create a clear and intuitive user interface.
Uses labels to display the title and the generated quote.

- Error Handling:
Provides user-friendly error messages in case the API request fails or encounters other issues.

- Code Modularity:
Organizes the code into a class (QuoteGenerator) to promote modularity and maintainability.

- Use of External Libraries:
Utilizes the requests library for making HTTP requests to the Quotable API.

- Initialization Function:
The __init__ method sets up the initial state of the application, including creating GUI elements and applying styles.

- Real-Time Feedback:
Updates the displayed quote in real-time, providing visual feedback to the user during the quote generation process.

- Cross-Platform Compatibility:
The code is designed to work on various platforms due to the use of the Tkinter library for GUI development.

- Application Entry Point:
The if __name__ == "__main__": block ensures that the application is executed when the script is run

## Authors

- [@Nawal-Shahid](https://github.com/Nawal-Shahid)

