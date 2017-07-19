print " Greetings, dear customer Thank you so much for your visit !"
print " BUMBER DELIVERY SERVICES "
# boxA small box 
# boxB medium box 
# boxC large size box 

#3 diferent vehicle deliveries and 3 diferent size of boxes we need find what vehicle shoudl we use it

print """
We Can Help you with Delivery !



      ++++
     /  __\          ++++                     
     \( oo          (___ \                     
     _\_o/           oo~)/
    / \|/ \         _\-_/_
   / / __\ \___    / \|/  \
   \ \|   |__/_)  / / .- \ \
    \/_)  |       \ \ .  /_/
     ||___|        \/___(_/
     | | |          | |  |
     | | |          | |  |
     |_|_|          |_|__|
     [__)_)        (_(___] 
     
"""
     
print " We will help you to choose Vehicle & Driver."
print " Looking Bicycle, Car or Cargo Van ? Easy as 1,2,3 ...  "
# constantas 
a_rate = 3
c_rate = 6
b_rate = 9

client_name = raw_input(" Please, type your name ")
client_name = client_name.upper()
adress_from = raw_input (" Please, type full adreess from where we need pick up your package .... ")
zipcode_from = raw_input( " please provide zip code of your location , type only numbers ....")
zipcode_from = int(zipcode_from)
adress_to = raw_input(" Please, type full adrees where we need drop your package ....")
zipcode_to = raw_input(" Please, provide destination zip code, type only numbers ....")
zipcode_to = int(zipcode_to)
dist_zip = zipcode_from - zipcode_to
print dist_zip
client_box_options = """

   What size of boxes do you have ? :

    A. Small Box / Boxes : size less 100"

    B. Medium size Box / Boxes : size over 100"

    C. Large size Box / Boxes : size over 250" 
    
    D. Extra Large Box/ Boxes : size over 400" 

"""
while True:

        answer = raw_input(client_box_options)

        answer = answer.upper()

        if answer == "A":
            qty_small = raw_input ( " How many Small boxes do you Have? ")
            qty_small = int(qty_small)
            print "Here your delivery cost $ ..."
            
            a_price_cost = qty_small * dist_zip * a_rate
            print a_price_cost 
            print " " +  "Dear" + client_name + " Bicycle Driver on His Way"
            print """
                                                $"   *.      
              d$$$$$$$P"                  $    J
                  ^$.                     4r  "
                  d"b                    .db
                 P   $                  e" $
        ..ec.. ."     *.              zP   $.zec..
    .^        3*b.     *.           .P" .@"4F      "4
  ."         d"  ^b.    *c        .$"  d"   $         %
 /          P      $.    "c      d"   @     3r         3
4        .eE........$r===e$$$$eeP    J       *..        b
$       $$$$$       $   4$$$$$$$     F       d$$$.      4
$       $$$$$       $   4$$$$$$$     L       *$$$"      4
4         "      ""3P ===$$$$$$"     3                  P
 *                 $                  p                -
  *             ''                    ''             ''
    ""         ll                      ^%.        .r"
       "*==*""                             ^"*==*""  
       

            
            
        """

    

        elif answer == "B":
            qty_med = raw_input ( " How many Medium boxes do you Have? ")
            qty_med = int(qty_med)
            print " Here your delivery cost $ ..." 
                 
            b_price_cost = qty_med * dist_zip * b_rate
            print b_price_cost
            print """
                                  ___..............._
             __.. ' _'.""""""\\""""""""- .`-._
 ______.-'         (_) |      \\           ` \\`-. _
/_       --------------'-------\\---....______\\__`.`  -..___
| T      _.----._           Xxx|x...           |          _.._`--. _
| |    .' ..--.. `.         XXX|XXXXXXXXXxx==  |       .'.---..`.     -._
\_j   /  /  __  \  \        XXX|XXXXXXXXXXX==  |      / /  __  \ \        `-.
 _|  |  |  /  \  |  |       XXX|""'            |     / |  /  \  | |          |
|__\_j  |  \__/  |  L__________|_______________|_____j |  \__/  | L__________J
     `'\ \      / ./__________________________________\ \      / /___________\
        `.`----'.'   dp                                `.`----'.'
          `_____                                              ADESIGNSTORE.COM
            
            """

            

        elif answer == "C":
            qty_lar = raw_input ( " How many Large boxes do you Have? ")
            qty_lar = int(qty_lar)
            print " Here your delivery cost $ ..." 
                 
            c_price_cost = qty_lar * dist_zip * c_rate
            print c_price_cost
            print """
                                                          ____
                             ______...-----'_'____\.
             _____.....----==---'\|-----''''        \
            /--------'''''  ____ |                   \
           /  __..--- | .-''    \|\                   \-___
          /| |       || |     __ | \           ____..-'    `---._
         //  |       || |    [__]| |__...----''                  `-.__
 _______//|  |       || |______\\| \ == _____         ____..---''''   \
/_______/ |  `-------'|         `\  |==.     ``---.--'   .-\\\\\\\\\| )
|         | [-]       |[-]          | //          | [ ] (  )|||||||||_'|
|         \           |             |// .-------   \_____`.----''  \ ()|
|    _____ \          |         ___ |` /    ____\_   |   (_) |__..-'   |
\   /     \ \  ____..-| -----'''    | /  .-'      `-_|_               _|
|  /  _--'-\ \         \            | | /    ___     \ |  ____:F_P:-''/
| |  /---_    `-.______|__...------'/ //  .-'   `\    \|_/      __/_-/
 \| / .-. \   _ `--..__\___...-----' | |  |  .-.  |   | ____---'/    |
   | /   \ \  \`-_____....-----------'_|  | (   ) |   |     `--'    /
   | | ( )| |  |__\________/__..-'     \  \  `-'  /   |-'\         /
   \ \    / |  |       \_     _/        \  `-.__.'   /    `--.__.-'
    \ `--' /  /          `---'           \_        _/
     \____/__/     ADESIGNSTORE.COM
            
            """

          


        else:

            print " Sorry, you need find Truck Delivery Company, please call 888-TRUCKON ?" 
            print """
            .
    .  .
    .  .   .    __                      __
          .     ||______________________||
       .    .   ||  __________________  ||
              / || |           (__)   | ||
        .   . / || |           (oo)   | ||
            |  -|| |           _\/_   | ||
        .   . \ || |=---------/(())\-\| ||
            (\  |\-----------------------\
        .    (\ || \_______________________\
               \||  |                       |
         .      \|  | (O) |-----------| (O) | .
                 \  |     |-----------|     |       .
          .       \ |       TRUCKON       |  .
                   \|                       |
            .      (=========================)
                    |_||_|             |_||_|
                                           ADESIGNSTORE.COM
               .                                 \

                  .                                  \
                  """
            break
        
        
print "Dear" + client_name + " ! " 
print " Thank you so much for your business with us! We really Happy to help you " 
print " Will be delivered from " + adress_from + " to" + "  "  + adress_to 
print " You will receive delivery link via email in next 2-10 minutes"