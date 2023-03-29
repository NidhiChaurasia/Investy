from django.shortcuts import render

# Create your views here.
def input(request):
    
    return render(request,'input.html')

def output(request):
    
    return render(request,'output.html')

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