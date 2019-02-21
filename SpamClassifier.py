import os

work_dir = "C:\\Users\\kamle\\OneDrive\\Documents\\Projects\\Learning Material\\Codes\\ApacheSpamClassifier\\"


# Getting emails from all file contained in a particular folder
emails_list = []
labels = []
def get_emails(folder_name, label=None):
    work_dir = "C:\\Users\\kamle\\OneDrive\\Documents\\Projects\\Learning Material\\Codes\\ApacheSpamClassifier\\" + folder_name + "\\"
    file_list = os.listdir(work_dir)
    for file_name in file_list:
        try:
            file = open(work_dir + file_name, 'r')
            emails_list.append(file.read())
            labels.append(label)
        except:
            pass
    #return emails_list, [label]*len(emails_list)


get_emails("spam_2", 1)
get_emails("easy_ham_2", 0)
get_emails("hard_ham", 0)

len(emails_list)==len(labels)

# Spliting Training and test data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(emails_list, labels, random_state=42)




#TODO: create a transformer which converts all emalis into a sparse matrix (indicating presence or absence of words)
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
encoder.fit_transform(X_train)

#TODO: add parameter to transformer
from sklearn.base import BaseEstimator, TransformerMixin

