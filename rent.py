#goal is to figure out how much rent i can pay per month
#inputs are how much aid i get per month for rent, for the academic year
#other input is how much money id have out of my own pocket
#other input is how long the lease is going to be
total_aid = int(input("How much aid are you receiving?: "))
loans = int(input("How much are you getting from loans?: "))
own_money = int(input("How much of your own money?: "))
lease_duration = int(input("How many months is the lease?: "))
deposit = int(input("How much is the security deposit?: "))

yearly_tuition = 14025
health_insurance = 2922

resulting_aid = total_aid + loans - yearly_tuition - health_insurance #gives us the leftover aid that we can work with
result = resulting_aid + own_money - deposit
result = result / lease_duration
print("With the given information, you have {} worth of resulting aid (after tuition and health insurance), you can pay {} per month at most on a {} month lease.".format(resulting_aid, result, lease_duration))