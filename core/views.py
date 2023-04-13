from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def input(request):
    
    return render(request,'input.html')

def output(request):
    


    if request.method == 'POST':
        # gender = request.POST.get('Gender')
        # age = request.POST.get('Age')
        # avenues = request.POST.get('Avenues')
        # mfr = request.POST.get('mfr')
        # emr = request.POST.get('emr')
        # dr = request.POST.get('dr')
        # gbr = request.POST.get('gbr')
        # fdr = request.POST.get('fdr')
        # pfr = request.POST.get('pfr')
        # goldr = request.POST.get('goldr')
        # rer = request.POST.get('rer')
        # cr = request.POST.get('cr')
        # factors = request.POST.get('Factors')
        # inobjectives = request.POST.get('InObjectives')
        # objectives = request.POST.get('Objectives')
        # stock_market = request.POST.get('StockMarket')
        # purpose = request.POST.get('Purpose')
        # instrument = request.POST.get('Instrument')
        # monitor = request.POST.get('Monitor')
        # return_rate = request.POST.get('Return')
        # most = request.POST.get('Mostly')
        # eq = request.POST.get('Equity')
        # mutual = request.POST.get('Mutual')
        # govt = request.POST.get('Government')
        # fd = request.POST.get('Fixed')
        # info = request.POST.get('Information')
        data_list = []
        data_list.append(request.POST.get('Gender'))
        data_list.append(request.POST.get('Age'))
        data_list.append(request.POST.get('Avenues'))
        data_list.append(request.POST.get('mfr'))
        data_list.append(request.POST.get('emr'))
        data_list.append(request.POST.get('dr'))
        data_list.append(request.POST.get('gbr'))
        data_list.append(request.POST.get('fdr'))
        data_list.append(request.POST.get('pfr'))
        data_list.append(request.POST.get('goldr'))
        data_list.append(request.POST.get('rer'))
        data_list.append(request.POST.get('cr'))
        data_list.append(request.POST.get('Factors'))
        data_list.append(request.POST.get('InObjectives'))
        data_list.append(request.POST.get('Objectives'))
        data_list.append(request.POST.get('StockMarket'))
        data_list.append(request.POST.get('Purpose'))
        data_list.append(request.POST.get('Instrument'))
        data_list.append(request.POST.get('Monitor'))
        data_list.append(request.POST.get('Return'))
        data_list.append(request.POST.get('Equity'))
        data_list.append(request.POST.get('Mutual'))
        data_list.append(request.POST.get('Government'))
        data_list.append(request.POST.get('Fixed'))
        data_list.append(request.POST.get('Information'))
        # print(data_list)
        import joblib

        cls=joblib.load('trained_model.sav')
        data = cls.predict([data_list])
        print('data  ',data[0])

        # data=[0]
        # ans=None
        if(data[0]==0):
            ans="Mutual Funds"
        elif(data[0]==1):
            ans='Equity Market'
        elif(data[0]==2):
            ans='Debentures'
        elif(data[0]==3):
            ans='Government Bonds'
        elif(data[0]==4):
            ans='Fixed Deposits'
        elif(data[0]==5):
            ans='Public Provident Fund'
        elif(data[0]==6):
            ans='Gold'
        elif(data[0]==7):
            ans='Real Estate'
        elif(data[0]==8):
            ans='Cryptocurrency'

        high_values,low_values,date_list=None,None,None
        high_values,low_values,date_list=getGraphData(request)
        # print(high_values)
        # print(date_list)
        
        return render(request,'output.html',{"data":ans,"high_values":high_values,"low_values":low_values,"date_list":date_list,"show":True})
    
    return render(request,'input.html')


def getGraphData(request):
    import requests
    import datetime
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"symbol":"MSFT","function":"TIME_SERIES_MONTHLY","datatype":"json"}

    headers = {
        "X-RapidAPI-Key": "31479a3ea9mshb6c0e982e626d10p1053aajsned036f0a8246",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    data=response.json()

    monthly_time_series = data["Monthly Time Series"]

    current_year = datetime.datetime.now().year
    years_ago = 5
    five_years_ago = current_year - years_ago

    # Extract the last 5 years of data
    last_5_years_data = {date: values for date, values in monthly_time_series.items() if int(date.split('-')[0]) >= five_years_ago}

    # Extract all the high values from the last 5 years of data
    high_values = [float(val["2. high"]) for val in last_5_years_data.values()]
    low_values = [float(val["3. low"]) for val in last_5_years_data.values()]
    date_list = [datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%b %Y") for date in last_5_years_data.keys()]

    print("Exact month and year from the data:",len(date_list))
    print("All high values from the last 5 years:", len(high_values))
    # print("All low values from the last 5 years:", low_values)

    # # Extract all the '2. high' values from the 'Monthly Time Series' dictionary
    # high_values = [float(val["2. high"]) for val in monthly_time_series.values()]

    # print("All high values:", high_values)
    high_values.reverse()
    low_values.reverse()
    date_list.reverse()
    return high_values,low_values,date_list

'''
import random
import csv

# Define possible values for each column
GENDERS = ["Male", "Female"]
INVEST_A = ["Yes", "No"]
INVEST_BEST_OPTIONS = [
    "Mutual Funds",
    "Equity Market",
    "Debentures",
    "Government Bonds",
    "Fixed Deposits",
    "Public Provident Fund",
    "Gold",
]
INVEST_FACTOR = [
    "Returns",
    "Locking Period",
    "Risk",
]
INVEST_OBJECTIVE = [
    "Capital Appreciation",
    "Income",
    "Growth",
]
INVEST_PURPOSE = [
    "Wealth Creation",
    "Savings for Future",
    "Returns",
]

EQUAITY_REASONS = [
    "Capital Appreciation",
    "Dividend",
    "Liquidity",
]
MUTUAL_REASONS = [
    "Better Returns",
    "Tax Benefits",
    "Fund Diversification",
]
GOVT_REASONS = [
    "Safe Investment",
    "Safe Investment",
    "Tax Incentives",
]
FD_REASONS = [
    "Risk Free",
    "High Interest Rates",
    "Fixed Returns",
]
OBJECTIVE_OPTIONS = [
    "Retirement Plan",
    "Health Care",
    "Education",
    # "Marriage",
    # "Buying Property",
    # "Travel",
    # "Savings",
]
DURATION_OPTIONS = ["Less than 1 year", "1-3 years", "3-5 years", "More than 5 years"]
MONITOR_OPTIONS = ["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"]
RETURN_OPTIONS = ["10%-20%", "20%-30%", "30%-40%"]
INVEST_AVENUE_OPTIONS = [
    "Mutual Funds",
    "Equity Market",
    "Debentures",
    "Government Bonds",
    "Fixed Deposits",
    "Public Provident Fund",
    "Gold",
]
SAVINGS_OPTIONS = [
    "Retirement",
    "Children's Education",
    "Emergency Fund",
    "Buying Property",
    "Vacation",
    "Marriage",
    "Others",
]
INFO_SOURCES = [
    "Newspapers and Magazines",
    "Internet",
    "Financial Consultants",
    "Television",
    "Friends and Family",
]


# Generate random data for n rows
data = []
for i in range(100000):
    gender = random.choice(GENDERS)
    age = random.randint(18, 65)
    invest_a = random.choice(INVEST_A)
    # mutual_rank = random.randint(1, 7)
    # equity_rank = random.randint(1, 7)
    # debentures_rank = random.randint(1, 7)
    # gover_bonds_rank = random.randint(1, 7)
    # fd_rank = random.randint(1, 7)
    # pf_rank = random.randint(1, 7)
    # gold_rank = random.randint(1, 7)
    rankings = random.sample(range(1, 8), 7)

    mutual_rank = rankings[0]
    equity_rank = rankings[1]
    debentures_rank = rankings[2]
    gover_bonds_rank = rankings[3]
    fd_rank = rankings[4]
    pf_rank = rankings[5]
    gold_rank = rankings[6]

    do_stock = random.choice(GENDERS)
    invest_F = random.choice(INVEST_FACTOR)
    invest_O = random.choice(INVEST_OBJECTIVE)
    invest_P = random.choice(INVEST_PURPOSE)
    duration = random.choice(DURATION_OPTIONS)
    monitor = random.choice(MONITOR_OPTIONS)
    return_option = random.choice(RETURN_OPTIONS)
    invest_avenue = random.choice(INVEST_AVENUE_OPTIONS)
    objective_options = random.choice(OBJECTIVE_OPTIONS)
    reasons_equity = random.choice(EQUAITY_REASONS)
    reasons_mutual = random.choice(MUTUAL_REASONS)
    reasons_government = random.choice(GOVT_REASONS)
    reasons_fixed = random.choice(FD_REASONS)
    info_sources = random.choice(INFO_SOURCES)

    # factor_options = random.sample(FACTOR_OPTIONS, len(FACTOR_OPTIONS))
    # savings_objectives = random.sample(SAVINGS_OPTIONS, len(SAVINGS_OPTIONS))

    row = (
        gender,
        age,
        invest_a,
        mutual_rank,
        equity_rank,
        debentures_rank,
        gover_bonds_rank,
        fd_rank,
        pf_rank,
        gold_rank,
        do_stock,
        invest_F,
        invest_O,
        invest_P,
        duration,
        monitor,
        return_option,
        invest_avenue,
        objective_options,
        reasons_equity,
        reasons_mutual,
        reasons_government,
        reasons_fixed,
        info_sources,
    )
    data.append(row)

# Write data to CSV file
with open("test3.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(
        [
            "GENDER",
            "AGE",
            "Do you invest in Investment Avenues?",
            "What do you think are the best options for investing your money? (Rank in order of preference) [Mutual Funds]",
            "What do you think are the best options for investing your money? (Rank in order of preference) [Equity Market]",
            "What do you think are the best options for investing your money? (Rank in order of preference) [Debentures]",
            "What do you think are the best options for investing your money? (Rank in order of preference) [Government Bonds]",
            "What do you think are the best options for investing your money? (Rank in order of preference) [Fixed Deposits]",
            "What do you think are the best options for investing your money? (Rank in order of preference) [Public Provident Fund]",
            "What do you think are the best options for investing your money? (Rank in order of preference) [Gold]",
            "Do you invest in Stock Market?",
            "What are the factors considered by you while investing in any instrument?",
            "What are your investment objectives?",
            "What is your purpose behind investment?",
            "How long do you prefer to keep your money in any investment instrument?",
            "How frequently do you monitor your investments?",
            "How much return do you expect from any investment instrument?",
            "Which investment avenue do you mostly invest in?",
            "What are your savings objectives?",
            "Reasons for investing in Equity Market",
            "Reasons for investing in Mutual Funds",
            "Reasons for investing in Government Bonds",
            "Reasons for investing in Fixed Deposits",
            "Your sources of information for investments is",
        ]
    )
    writer.writerows(data)
'''