# Docker MLOps Activity

-1.3, -4.8, 6.4, 0.3 = Valid bank note example


If you want to run docker

1) docker build -t my-ml-app .
2) docker run -d -p 8000:5000 my-ml-app
3) http://localhost:8000/

To stop it

1) docker ps
2) docker stop <container_id>


If you want to run the code itself locally

1) Uncomment the pywin32 package in requirements.txt (if in windows)
2) pip install -r requirements.txt
3) uvicorn app:app --reload