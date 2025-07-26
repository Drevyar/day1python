print('===================== Personal Finance Calculator =====================')
print('kraivich Sammalertphan 6730202050')
print('21 july 2025')

while True:
    try:
        monthly_income = float(input('How much is your monthly income? THB : '))
        if monthly_income < 0:
            print('Please try again.')
            continue  #ถ้าค่า monthly_income ติดลบให้ถามใหม่
        if monthly_income == 0:
            print('Monthly income can not be zero.')
            continue

        rent_cost = input('Do you pay rent or a mortgage for your house? (yes/no): ').strip().lower() #.strip #.lower เปลี่ยนเป็นตัวเล็กทั้งหมด
        if rent_cost not in ['yes', 'no']: #ถ้าคำตอบไม่ใช่ yes no ให้ถามใหม่
            print('Please answer "yes" or "no".')
            continue
        if rent_cost == 'no':
            rent_cost = 0.0
        else:
            rent_cost = float(input('How much is the monthly rent for the house? THB : '))
            if rent_cost < 0:
                print('Please try again.')
                continue
        
        food_budget = int(input('How much is your monthly food expense? THB :'))
        if food_budget < 0:
            print('Please try again.')
            continue
        
        transportation_cost = float(input('How much is your monthly transportation expense? THB :'))
        if transportation_cost < 0:
            print('Please try again.')
            continue
        
        entertainment_budget = int(input('How much is your monthly recreation expense? THB :'))
        if entertainment_budget < 0:
            print('Please try again.')
            continue
        
        emergency_fund_percent = float(input('What percent of your income do you set aside for emergencies? (%): '))
        if emergency_fund_percent < 0 or emergency_fund_percent > 100:
            print('Please try again.')
            continue
        
        investment_percent = float(input('What percent of your income do you invest monthly? (%): '))
        if  investment_percent < 0 or investment_percent > 100:
            print('Please try again.')
            continue
        
        total_fixed_expenses = rent_cost + transportation_cost #ค่าใช้จ่ายคงที่
        total_variable_expenses = food_budget + entertainment_budget #ค่าใช้จ่ายไม่คงที่
        total_expenses = total_fixed_expenses + total_variable_expenses #ค่าใช้จ่ายทั้งหมด
        
        if total_expenses > monthly_income: #เช็คว่า  total_expenses > monthly_income มั้ยถ้ามากกว่าให้กรอกใหม่
            print('Your total more than  your income.')
            continue
        
        
        remaining_income = monthly_income - total_expenses #รายได้คงเหลือ
        emergency_amount = monthly_income * (emergency_fund_percent / 100) #เงินฉุกเฉิน
        investment_amount = monthly_income  * (investment_percent / 100) #เงินลงทุน
        
        if emergency_amount + investment_amount > remaining_income:
            print('Savings and investments morethan income.')
            continue
        
        
        available_savings = remaining_income - emergency_amount - investment_amount #เงินเหลือสำหรับออม
        expense_ratio = (total_expenses / monthly_income) * 100 #สัดส่วนค่าใช้จ่ายต่อรายได้
        
        print('\n=== MONTHLY BUDGET REPORT ===')
        print(f'Income : {monthly_income:,.2f} THB')
        print(f'Fixed Expenses : {total_fixed_expenses:,.2f} THB')
        print(f'Variable Expenses : {total_variable_expenses:,.2f} THB')
        print(f'Total Expenses : {total_expenses:,.2f} THB')
        print(f'Remaining : {remaining_income:,.2f} THB')
        
        print('\n\n=== SAVING BREAKDOWN ===')
        print(f'Emergency Fund ({emergency_fund_percent:.2f}%) : {emergency_amount:,.2f} THB')
        print(f'Investment ({investment_percent:.2f}%) : {investment_amount:,.2f} THB')
        print(f'Available for Savings : {available_savings:,.2f} THB')
        
        print('\n\n=== ANALYSIS ===')
        print(f'Expense Ratio : {expense_ratio:,.2f}%')
        
        break #ถ้าค่าทั้งหมดถูกให้ออกจาก loop
    except ValueError:
        print('Invalid input. Please enter a valid number.')dwdw