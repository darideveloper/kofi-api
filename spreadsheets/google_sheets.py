#! python3
# Conect to google spreadsheets
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SheetsManager (): 
    """ Class to conect to google shets and upload data"""

    def __init__ (self, google_sheet_link, creds_path, sheet_name=None): 
        """ Construtor of the class"""

        # Read credentials
        if not os.path.isfile (creds_path):
            raise FileNotFoundError ("The credential file path is not correct")
        
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        client = gspread.authorize(creds)

        # Conect to google sheet
        self.sheet = client.open_by_url(google_sheet_link)

        # Set the sheet 1 as worksheet
        if sheet_name:
            self.worksheet = self.sheet.worksheet(sheet_name)
        else:
            self.worksheet = self.sheet.sheet1

    def set_sheet (self, sheet_name:str):
        """ Change current working sheet

        Args:
            sheet_name (str): sheet name
        """
        
        self.worksheet = self.sheet.worksheet(sheet_name)

    def write_cell (self, value, row=1, column=1):
        """ Write data in specific cell 
        """
        self.worksheet.update_cell(row, column, value)

    def write_data (self, data, row=1, column=1): 
        """ Write list of data in the worksheet"""
        
        # check if data exist
        if not data: 
            print ("THERE IS NO NEW INFORMATION TO WRITE IN THE FILE.")
        else:
            print ("Writing information on spreadsheet...")

            # Loop for each row of data
            for row_data in data: 

                # Set the position of the next row. Omit the header
                row_index = data.index(row_data) + row
                
                for cell in row_data:
                    column_index = row_data.index (cell) + column
                    
                    self.write_cell (cell, row_index, column_index)

    def get_data (self): 
        """ Read all records of the sheet"""

        records = self.worksheet.get_all_records()
        return records

    def get_rows_num (self) -> int: 
        """ Get number of the rows in use """

        return len(self.worksheet.col_values(1))
    
    def get_cols_num (self) -> int: 
        """ Get number of the columns in use """

        return len(self.worksheet.rows_values(1))
