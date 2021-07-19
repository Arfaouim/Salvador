import pandas as pd
import numpy as np

def login_table(id_name_verified, id_password):
    """
    :param id_name_verified: (DataFrame) DataFrame with columns: Id, Login, Verified.   
    :param id_password: (numpy.array) Two-dimensional NumPy array where each element
                        is an array that contains: Id and Password
    :returns: (None) The function should modify id_name_verified DataFrame in-place. 
              It should not return anything.
    """   
    id_name_verified.drop(inplace=True, columns="Verified") # drop verified column inplace
    id_name_verified.insert(loc=2,column="Password",value=np.nan) # insert password column inplace
    for row in range(len(id_password)): 
        # apply the password on the rows that match using at
        id = id_password[row][0]
        pw = id_password[row][1]
        id_name_verified.at[row, "Password"] = pw

id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False]], columns=["Id", "Login", "Verified"])
id_password = np.array([[1, 987340123], [2, 187031122]], np.int32)
login_table(id_name_verified, id_password)
print(id_name_verified)