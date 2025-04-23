#2025-04-22, shw
# main.py

# 각 적금 상품별 최대 금액 기준으로 원금 + 이자를 계산

# 공통 정보
days = 31  # 한달 기준 31일
tax_rate = 0.154  # 이자 과세율 (15.4%)

# 상품 정보: (이름, 최대 일 입금액, 금리 연 %, 기간)
products = [
    ("카카오뱅크 한달적금", 30000, 7.00, days),
    ("OK저축은행 작심한달적금", 10000, 20.25, days),
    ("케이뱅크 궁금한적금", 50000, 7.20, days),
    ("한국투자저축은행 한달적금", 30000, 12.00, days),
    ("우리은행 N일적금", 30000, 5.20, days)
]

# 계산 함수
def calculate_total(principal_per_day, rate_annual, period_days):
    total_principal = principal_per_day * period_days
    rate_daily = rate_annual / 100 / 365
    interest = total_principal * rate_daily * period_days
    interest_after_tax = interest * (1 - tax_rate)
    total_amount = total_principal + interest_after_tax
    return round(total_principal), round(interest_after_tax), round(total_amount)

# 결과 계산
results = []
for name, max_daily, rate, period in products:
    principal, interest, total = calculate_total(max_daily, rate, period)
    results.append((name, principal, interest, total))

print(results)
