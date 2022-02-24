# Energy_Load_Estimates

**Overview:**

Example of building a regression model and deploying it with docker.

The dataset is available at https://archive.ics.uci.edu/ml/datasets/Energy+efficiency. 

You should be able to run the docker image and then curl the container by sending json containing the 
attributes of a new building and get a json response with the heating and cooling loads 
predicted by your trained model. 

### To use:
**Pull the docker image from here:**

`$ docker pull jbrandenburg/multioutput_rf_flask_app`

**Start the container:**

`$ docker run -d -p 5000:5000 multioutput_rf_flask_app`

**Verify connectivity:**

`$ curl http://0.0.0.0:5000/`

**You can submit building parameters using the following POST call:**

`$ curl -X POST -H "Content-Type: application/json" -d '{
    "Relative Compactness": 0.74,
    "Surface Area": 588.00,
    "Wall Area": 294.00,
    "Roof Area": 147.00,
    "Overall Height": 7.00,
    "Orientation": 5,
    "Glazing Area": 0.10,
    "Glazing Area Distribution": 1
}' http://0.0.0.0:5000/get_estimates`
