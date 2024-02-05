# Import the Enki library
import enki

# Set up the connection to your PyBossa server
# Replace 'your-api-key', 'http://your-pybossa-server.com', and 'example-project' with your actual API key, PyBossa server URL, and project short name
e = enki.Enki(api_key='8024d641-b843-46e8-8411-d9448d52b80c', endpoint='http://54.218.59.150:5000', project_short_name='upwork01', all=1)

# Retrieve ongoing tasks and their task runs
e.get_tasks(state='ongoing')
ongoing_results = e.get_task_runs()

# Retrieve completed tasks and their task runs
e.get_tasks(state='completed')
completed_results = e.get_task_runs()

# Print the results
print("Ongoing Results:", ongoing_results)
print("Completed Results:", completed_results)
