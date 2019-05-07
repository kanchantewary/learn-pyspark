#### warn util utils service sparkui could not bind on port 4040 attempting port 4041
reason - Every SparkContext launches a web UI, by default on port 4040, that displays useful information about the application. This includes:
If multiple SparkContexts are running on the same host, they will bind to successive ports beginning with 4040 (4041, 4042, etc).  
Solution that worked - Shut down and restarted the vm to clear any orphan processes. The warning did not come after that.

