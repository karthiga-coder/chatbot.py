# CHAT BOT
     
 A chat bot for the Insurance company (Zion) where customer/user can buy Car or Bike insurance policy or renew existing policy with Zion.

# Function: 
## Chat bot should be able to interact with the user to –
      o	get a new quote
      o	buy a policy (has a Zion Quote)
      o	renew his existing policy
      o	looking for documents for his existing policy
 ## For a new Quote
      •	Get his name and what insurance policy he is looking for (Car, Bike) – if he is new customer
      •	Generate a Quote Number  and provide a Quote document for the user to download
 ## Buy policy (for existing quote and new quote)
      • et the Quote number 
      o Validate and show “Invalid Quote number” if the format is not correct
      •	Provide a policy document for the user to download Renew existing policy
 ## renew existing policy
      •	Get his name and policy number 
      o	Provide a policy document for the user to download
# SAMPLE INPUT
          def new():
              global num, id, name1
               name1 = input("Enter your full name:")
               first = name1.split()

               alpha = random.sample(range(65, 90), 1)
               for i in alpha:
               ch = chr(i)

                 randomlist = random.sample(range(11111, 99999), 1)
                  for i in randomlist:
                   num = i

                   id = first[0].lower() + "-" + ch + "-" + str(num)
                    print(id)

                     writefh()
        
 # SAMPLE OUTPUT
            Bot : Hi!!Great to meet u!! your full name?
            user : I am KARTHIGA
            Bot : KARTHIGA ,zion is a great insurance provider for automoblies,You car/bike?
            user :BIKE
            -------------------------------------------------------
            Bot :  1.Get a new Quote
	               2.Buy a policy(has a Zion Quote)
	               3.Renew his Existing Policy
	               4.Looking for documents for his Existing Policy
            -------------------------------------------------------
            Choose your status: 1
            Enter your full name:KARTHIGA G
            karthiga-G-69334
            Are you sure you want to continue? Y/N
            user :Y
            -------------------------------------------------------
            Bot :   1.Get a new Quote
	                2.Buy a policy(has a Zion Quote)
	                3.Renew his Existing Policy
	                4.Looking for documents for his Existing Policy
            -------------------------------------------------------
            Choose your status: 2
            Bot : enter your full name:
            user :KARTHIGA G
            Bot : enter your policy number:
            user :karthiga-M-69334
            username found KARTHIGA G
            Bot : Do you want your Details? Y/N
            user :Y
            Bot : KARTHIGA G.txt
            Are you sure you want to continue? Y/N
            user :N
            Bot : Thank You





