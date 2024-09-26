from bs4 import BeautifulSoup
import requests
import sqlite3

from constant import SEARCH_ENGINE_URL

class SearchEngine:
    result = []
    
    def search(self, word):
        search_word = self.construct_word(word)
        
        def save(self,sw,sr):
            x = {sw:sr}
        
        result_text = " " 
        
        if search_word:
            Url = SEARCH_ENGINE_URL + search_word 
            result= requests.get(Url)
            if result.status_code == 200:
                data = BeautifulSoup(result.text,"html.parser")
                # for ptag in data.find_all('p'):
                #     print(ptag.get_text())
                # print(result.text) 
                for ptag in data.find_all('p'):
                    result_text += ptag.get_text()
                return(result_text)    
            elif result.status_code == 404:
                return Exception("Search parameter not found")
            
            elif result.status_code == 500:
                return Exception('A server error occured')
                
            else:
                print("Failed to retrieve page")

    def construct_word(self, word :str)->str:
        try:
            if word: 
               word = word.strip()
               return word.title().replace(" ", "_")
            else:
                raise Exception
        except:
               return None

class DB_Manager:
                    db = sqlite3.connect('test.db')

                    cursor = db.cursor()

                    cursor.execute("""
                                CREATE TABLE IF NOT EXISTS employee(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                firstname TEXT NOT NULL,
                                lastname TEXT NOT NULL,
                                email TEXT UNIQUE,
                                gender TEXT DEFAULT 'MALE'
                                )
                                """)



                    cursor.execute('''
                                INSERT INTO employee(firstname,
                                lastname,
                                email,
                                gender
                                ) 
                                VALUES (?,?,?,?)
                                ''',
                                
                                ('Kree','Jersey','kreejersey@gmail.com','MALE'))
                                


                    db.commit()
                    db.close()

                
                    
                

