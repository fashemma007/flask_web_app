from website import create_app

app = create_app()

if __name__ == '__main__': ## run the app only when the main.py file is run directly, not via import
    app.run(debug=True)