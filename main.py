from pyscript import document, display, HTML

# Naming all the members
g7 = {'Eren Jaeger', 'Mikasa Ackermann', 'Armin Arlelt'} 
g8 = {'Sasha Braus', 'Connie Springer', 'Jean Kirstein'}
g9 = {'Levi Ackermann', 'Erwin Smith', 'Hange Zoe'} 
g10 = {'Reiner Braun', 'Bertholdt Hoover', 'Annie Leonhart', 'Pieck Finger', 'Porco Galliard'}

def check(e): 
    # Get string values from input fields and combine into full name
    first = document.getElementById("firstname").value.strip()
    last = document.getElementById("lastname").value.strip()
    name = (first + " " + last).title()
    
    # Get all members using union
    all_members = g7 | g8 | g9 | g10
    
    # Add the name
    all_members.add(name)
    
    # Sort members by alphabetical order
    finalmembers = "<br>".join(sorted(all_members))
   
    # Getting the total amount of people in the club
    output_html = f"""<div>{finalmembers}<br><br><b>Number of Members: {len(all_members)}</b></div>"""
    
    # Display 
    display(HTML(output_html), target="result", append=False)
