from Api import routes
from waitress import serve

if __name__ == "__main__":
    serve(routes.app, host='0.0.0.0', port=5000)