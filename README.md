## Corona vaccine slots Availability API (python)
API to get the free slots in for vaccine in given {state}{district}{age limit: 18/45}

Required libraries
- requests
- flask

Command to run : 
> python getfreevaccineslots_wothout_mail.py

Output:

    * Serving Flask app "getfreevaccineslots_wothout_mail" (lazy loading)
    * Environment: production
     WARNING: This is a development server. Do not use it in a production deployment.
     Use a production WSGI server instead.
    * Debug mode: on
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 309-700-650
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)



Once this script runs you can try to go to any browser and type below URL: 
The initial URL (http://127.0.0.1:5000/) is taken from output of the previous ran command

##### http://127.0.0.1:5000/get_slots?state={state_name}&district={district_name}&age_limit={18/45}
### Example URL:
##### http://127.0.0.1:5000/get_slots?state=uttar pradesh&district=bareilly&age_limit=45
##### http://127.0.0.1:5000/get_slots?state=uttar%20pradesh&district=bareilly&age_limit=45
