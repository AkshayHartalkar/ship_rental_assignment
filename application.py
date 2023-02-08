pyfrom flask_app import create_app

# import app instance and initialize
app = create_app()

# start server on port 80
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)