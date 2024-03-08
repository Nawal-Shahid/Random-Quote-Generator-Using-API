import tkinter as tk
from tkinter import ttk
import requests

class QuoteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quote Generator")

        # Apply a themed style
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Create and configure GUI elements
        self.label = ttk.Label(root, text="Random Quote Generator", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.quote_display = ttk.Label(root, text="", font=("Helvetica", 12), wraplength=400)
        self.quote_display.pack(pady=20)

        self.generate_button = ttk.Button(root, text="Generate Quote", command=self.generate_quote)
        self.generate_button.pack(pady=10)

        # Set initial quote
        self.generate_quote()

    def generate_quote(self):
        # Fetch a random quote from the Quotable API
        url = "https://api.quotable.io/random"
        response = requests.get(url)
        
        if response.status_code == 200:
            # Extract the quote from the API response
            quote_data = response.json()
            quote = f"{quote_data['content']} - {quote_data['author']}"
            # Update the displayed quote
            self.quote_display.config(text=quote)
        else:
            self.quote_display.config(text="Failed to fetch quote. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteGenerator(root)
    root.geometry("500x300")  # Set initial window size
    root.mainloop()
