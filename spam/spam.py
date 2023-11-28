import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import tkinter as tk
from tkinter import messagebox
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('spam.csv', encoding='latin1')  # Change encoding if necessary

# Prepare the data
X = data['v2']  # Input messages
y = data['v1']  # Labels (0 for non-spam, 1 for spam)

# Convert messages into numerical feature vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the SVM model
svm_model = SVC(kernel='linear')  # 'linear' kernel is used here
svm_model.fit(X_train, y_train)

# Function to perform prediction
def check_spam():
    user_message = entry.get()  # Get the user input

    # Search the message in the database
    index = data[data['v2'] == user_message].index
    if len(index) > 0:  # If the message is found in the database
        label = data.at[index[0], 'v1']  # Get the label from the database
        if label == 'spam':
            result = "The message is spam."
        else:
            result = "The message is not spam ('ham')."
    else:
        # If the message is not in the database
        user_message_vectorized = vectorizer.transform([user_message])  # Vectorize the message
        prediction = svm_model.predict(user_message_vectorized)  # Predict whether the message is spam or not
        if prediction[0] == 1:
            result = "The message is predicted as spam."
        else:
            result = "The message is predicted as not spam ('ham')."

    messagebox.showinfo("Spam Detection Result", result)  # Display the prediction in a message box


# Create a GUI window
window = tk.Tk()
window.title("Spam Detection System")
window.geometry("600x300")  # Set window size to 600x300 (width x height)

# Create a label and an entry for user input
label = tk.Label(window, text="Enter your message:")
label.pack()

# Create a larger entry for user input
entry = tk.Entry(window, width=60)  # Width of 60 characters
entry.pack()

# Create a button to check for spam
button = tk.Button(window, text="Check for Spam", command=check_spam)
button.pack()

# Run the main window loop
window.mainloop()
#spam:Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's
#ham:Ok lar... Joking wif u oni...