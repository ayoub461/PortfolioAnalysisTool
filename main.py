#Support Library
import sys
import os 
import p_Supportfunction as psf
#Pandas Library
import pandas as pd

def main ():
       
    elements_number = psf.get_int_positive("How much elemwent ")
    print("\nFile must be in the Downloads Directory\n")

    """Data Cleaning, And Formating"""

    #creating lsit of dictionnaries for storing the data frames
    closing = {}
    weights = []
    
    #Eterating over the Files
    for i in range(elements_number):
        
        #Getting names ans wieghts
        file_input = input("What is the file name (case sensitive): ")
        W = psf.get_percentage("Its Wieght : ")
        weights.append(W)
        
        #Create a path
        file_name = f"{file_input}.csv"
        file_path = os.path.join('C:/Users/dl/Downloads', file_name)
        try :
            #Read File 
            file_read = pd.read_csv(file_path)
            df_file_read = pd.DataFrame(file_read)
            
            #Set Date as index
            if i == 0 :
                closing["Date"] = df_file_read["Date"]
            
            #Formating "Adj Close" to Numeric data
            closing[file_input] = pd.to_numeric(df_file_read["Adj Close"])
        
        except FileNotFoundError:
            print(f"File {file_name} not found in Downloads directory.")
            continue
    
        except KeyError:
            print(f"Column 'Adj Close' not found in {file_name}. Skipping...")
            continue
    
        except Exception as e:
            print(f"An error occurred while processing {file_name}: {e}")
            continue

    #Into Pandas Data Frame
    closing_df = pd.DataFrame(closing)
    #Formating "Date" into Data data type
    try :
        closing_df["Date"] = pd.to_datetime(closing_df["Date"])
    except ValueError:
        raise ValueError("Datetime conversion error happens")
    except Exception as e:
        raise pd.errors.ParserError(f"Parsing a date from string fails: {e}")
        
       
    try: 
        #Set "Date" Column as Index
        closing_df.set_index("Date", inplace=True)
        #Drop the Nan/Na rows
        closing_df.dropna(inplace=True)
    except Exception as e:
        raise RuntimeError (f"Error in Indexting Date or Dropping NaN/Na{e}")
   
    
    """Calculate the Daily Return for each Stock"""

    portfolio = {}
    for key in closing_df.columns: 
        #Formating name:
        Return_name = f"{key}_return"
        #Daily return
        closing_df[Return_name] = (closing_df[key].pct_change().shift(-1))*100
        column_Return = closing_df[Return_name].mean()
        #Store it to Portofolio details
        portfolio[key] =[column_Return] 

    df_portfolio = pd.DataFrame(portfolio)
    # Drop NaN values (rows with missing data)
    
    """portfolio Return"""
    df_portfolio["portfolio_Return"] =[(df_portfolio * weights).sum().sum()]
   
    try :
        with open("Potofolio_Analysis.csv", "w") as file_p :
            file_p.write(f"\n\n{df_portfolio}")
    except OSError :
        raise OSError("Open file Failed")

if __name__ == "__main__":
    main()