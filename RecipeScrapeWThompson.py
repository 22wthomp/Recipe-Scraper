import tkinter as tk
from tkinter import filedialog 
from bs4 import BeautifulSoup
import requests

class recipeScrapeGUI:
   
    def __init__(self):
        #main window
        self.root = tk.Tk()
        self.root.title("Recipe Scraper")
        self.root.geometry("500x500")
        #Scroll bar canvas 
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side =tk.LEFT, fill= tk.BOTH, expand=True)
        #Scroll bar
        self.scrollbar = tk.Scrollbar(self.root, orient= tk.VERTICAL, command= self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill= tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        #The inner frame
        self.innerFrame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.innerFrame, anchor="nw")
        #configure the innerFrame
        self.innerFrame.bind("<Configure>", self.onFrameConfigure)
        #label
        self.label= tk.Label(self.innerFrame, text="Please enter the Url of the recipe", font=('Arial', 15))
        self.label.pack(padx=10,pady=10)
        #entry bar
        self.entry = tk.Entry(self.innerFrame ,font =('Arial', 10),width=50)
        self.entry.pack(padx=30, pady=10)
        #Scrape button
        self.button = tk.Button(self.innerFrame, text="Scrape Recipe", command=self.displayText)
        self.button.pack(pady=20)
        
        

        self.root.mainloop()
       
    def onFrameConfigure(self,event):
        self.canvas.configure(scrollregion= self.canvas.bbox("all"))
        
        
    def displayText(self):
        ingredients, instructions = self.scrapeRecipe()
        myFormat = ["Ingredients:\n","\nInstructions:\n"]
        if ingredients != None or instructions != None:
            #Creates box that output is put in
            self.box = tk.Text(self.innerFrame, height=30, width=60, font=('Arial', 12))
            self.box.pack(padx=10, pady=10)
            #creates bold tag for labels in box
            self.box.tag_configure("bold", font=('Arial', 14, 'bold'))
            #inserts ingredients label in box
            self.box.insert(tk.END,f"{myFormat[0]}\n",'bold')
            for x in ingredients:
                self.box.insert(tk.END, f"{x.text}\n")
            self.box.insert(tk.END,f"\n{myFormat[1]}\n",'bold')
            for y in instructions:
                self.box.insert(tk.END, f"{y.text}\n\n")
            self.button = tk.Button(self.innerFrame, text="Save Recipe", command=lambda :self.saveRecipe(instructions,ingredients))
            self.button.pack(pady=20)
    
    def saveRecipe(self,ingredients,instructions):
        #filepath window 
        filePath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save file as"
        )
        #if they chose a filepath it will then write to the filename given
        if filePath:
            file = open(filePath,'w')
            self.instructions =[file.write(y.text+'\n') for y in instructions]
            self.ingredients =[file.write(x.text+'\n') for x in ingredients]
            
    def scrapeRecipe(self):
        urlName = self.entry.get()
        if 'thepioneerwoman.com' in urlName:
            return self.pioneerScrape(urlName)
        elif 'allrecipes.com' in urlName:
            return self.allRecipesScrape(urlName)
        elif 'wellplated.com' in urlName:
            return self.wprmScrape(urlName)
        #elif 'thewoksoflife.com' in urlName:
            #return self.wprmScrape(urlName)
        else:
            self.Error = tk.Label(self.innerFrame,text ="This website is not currently supported")
            self.Error.pack(pady=0)
            
    def allRecipesScrape(self,urlName):
        #requests the page using the urlName
        page_to_scrape = requests.get(urlName)
        #grabs the html from this
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        #parses the html and looks for li tags with the specified class adds it to a list
        ingredients = soup.findAll("li",attrs={"class": "mm-recipes-structured-ingredients__list-item"})
        instructions = soup.findAll("p", attrs={"class": "comp mntl-sc-block mntl-sc-block-html"})
        #returns what is found
        return ingredients, instructions
    
    def wprmScrape(self,urlName):
        #same code as allRecipesScrape due to having similar html structure but website had different class names
        page_to_scrape = requests.get(urlName)
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        ingredients = soup.findAll("li",attrs={"class": "wprm-recipe-ingredient"})
        instructions = soup.findAll("div", attrs={"class": "wprm-recipe-instruction-text"})
        return ingredients, instructions
    
    def pioneerScrape(self,urlName):
        page_to_scrape = requests.get(urlName)
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        ingredients = soup.findAll("li",attrs={"class": "css-1tysp77 e12sb1171"})
        #This website has a different html structure than the others 
        #finds all the elements that contains li
        liParents = soup.find_all('li')
        #loops throught the li elements of the list to find a ol that matches the class name
        for liParent in liParents:
            ol = liParent.find('ol',class_='css-1r2vahp emevuu60')
            #if it finds a matching ol then it finds all of the li tags contained in it and adds it to instructions
            if ol:
                instructions = ol.find_all("li")
        return ingredients, instructions
recipeScrapeGUI()









