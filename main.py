#Sare modules ko combine karne wala code
import os

print("\n Running Data Preprocessing...")
os.system("python data_preprocessing.py")

print("\n Running Visualization...")
os.system("python data_visualization.py")

print("\n Running Model Training...")
os.system("python model_training.py")

print("\n Running Model Evaluation...")
os.system("python model_evaluation.py")

print("\n Running Queries...")
os.system("python queries.py")
