from flask import Flask, request
from .calculate_profit_service import calculate_profit


# template function to define routes and endpoints 
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    # load the test config if passed in
    app.config.from_mapping(test_config)

    """
        Hello page for indication of running webserver, all undefined endpoints fall back to hello page
    """
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return """<h3>Application is running.</h3>
        <p>Available endpoints</p>
        <ul>
        <li>/spaceship/optimize [POST] </li>
        </ul>
        """

    @app.route('/spaceship/optimize', methods=['POST'])
    def spaceship_optimize():
        """
            simple post endpoint handler
            @body - raw json;
            eg: [{"name": "Contract1", "start": 0, "duration": 5, "price": 10}, 
            {"name": "Contract2", "start": 3, "duration": 7, "price": 14}]

            @output: json;
            eg: {"income": 18, "path": ["Contract1", "Contract3"]}
        """
        contracts = request.get_json()
        response = calculate_profit(contracts)
        return response

    return app